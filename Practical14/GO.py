from xml.dom.minidom import parse as xml_parse
import xml.dom.minidom as xdm
import xml.sax as xs
import time as tm

# DOM
begin_time = tm.time() # Time recording
dom_data = xdm.parse(r"C:/Users/wym/Desktop/wym/IBI1_2024-25/Practical14/go_obo.xml") # Parse the xml file
root_element = dom_data.documentElement
all_terms = root_element.getElementsByTagName("term")

# Initialize dictionary for storing results
ontology_results = {
    "molecular_function": [],
    "biological_process": [],
    "cellular_component": []
}

max_values = {
    "molecular_function": 0,
    "biological_process": 0,
    "cellular_component": 0
}

# Count the maximum "is_a" ​for terms in each namespace using ​DOM.
for current_term in all_terms:
    ns = current_term.getElementsByTagName("namespace")[0].firstChild.nodeValue
    identifier = current_term.getElementsByTagName("id")[0].firstChild.nodeValue
    term_name = current_term.getElementsByTagName("name")[0].firstChild.nodeValue
    parent_relations = current_term.getElementsByTagName("is_a")
    relation_count = len(parent_relations)
    
# Updates max is_a terms: replace if higher, append if equal.
    if ns in ontology_results:
        if relation_count > max_values[ns]:
            ontology_results[ns] = [(identifier, term_name, relation_count)]
            max_values[ns] = relation_count
        elif relation_count == max_values[ns]:
            ontology_results[ns].append((identifier, term_name, relation_count))

print("DOM Parser Output:") # This classifys the output (like a title), which is clearer.
for namespace, term_data in ontology_results.items():
    print(f"Category: {namespace}")
    for term_id, term_desc, term_count in term_data:
        if term_count == max_values[namespace]:
            print(f"  Identifier: {term_id}")
            print(f"  Description: {term_desc}")
            print(f"  Parent Relations: {term_count}\n")
end_time = tm.time()
dom_duration = end_time - begin_time
print(f"DOM processing time: {dom_duration:.2f} seconds")

# SAX parser set up
class OntologyHandler(xs.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.term_id = ""
        self.term_name = ""
        self.term_ns = ""
        self.parent_count = 0
        self.results = {
            "molecular_function": [],
            "biological_process": [],
            "cellular_component": []
        }
        self.max_counts = {
            "molecular_function": 0,
            "biological_process": 0,
            "cellular_component": 0
        }
        self.temp_data = {
            "name": "",
            "ns": "",
            "id": ""
        }
        self.in_term = False
        self.processing_name = False

    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == "term":
            self.in_term = True
            self.term_id = ""
            self.term_name = ""
            self.term_ns = ""
            self.parent_count = 0
            self.temp_data = {"name": "", "ns": "", "id": ""}
        elif tag == "name":
            self.processing_name = True
        elif self.current_tag == "is_a":
            self.parent_count += 1

    def characters(self, content):
        if not self.in_term:
            return
        if self.current_tag == "id":
            self.temp_data["id"] += content
        elif self.current_tag == "namespace":
            self.temp_data["ns"] += content
        elif self.processing_name:
            self.temp_data["name"] += content

    def endElement(self, tag):
        if tag == "namespace":
            self.term_ns = self.temp_data["ns"].strip()
        elif tag == "id":
            self.term_id = self.temp_data["id"].strip()
        elif tag == "name":
            self.term_name = self.temp_data["name"].strip()
            self.processing_name = False
        elif tag == "term":
            if self.term_ns in self.results:
                if self.parent_count > self.max_counts[self.term_ns]:
                    self.results[self.term_ns] = [(self.term_id, self.term_name, self.parent_count)]
                    self.max_counts[self.term_ns] = self.parent_count
                elif self.parent_count == self.max_counts[self.term_ns]:
                    self.results[self.term_ns].append((self.term_id, self.term_name, self.parent_count))

# SAX execution
start_time = tm.time()
sax_parser = xs.make_parser()
sax_parser.setFeature(xs.handler.feature_namespaces, False)
handler = OntologyHandler()
sax_parser.setContentHandler(handler)
sax_parser.parse(r"C:/Users/wym/Desktop/wym/IBI1_2024-25/Practical14/go_obo.xml")

print("SAX Parser Output:")
for ns, terms in handler.results.items():
    print(f"Category: {ns}")
    for t_id, t_name, t_count in terms:
        if t_count == handler.max_counts[ns]:
            print(f"  Identifier: {t_id}")
            print(f"  Description: {t_name}")
            print(f"  Parent Relations: {t_count}\n")

end_time = tm.time()
sax_duration = end_time - start_time
print(f"SAX processing time: {sax_duration:.2f} seconds")

# Rate comparison
if sax_duration < dom_duration:
    print("SAX was the quickest")
else:
    print("DOM was the quickest")
# Comment: SAX was the quickest