from rdflib import Graph, Namespace

# whether to parse graph again
parse_graph = False

# graph
if parse_graph:
    graph = Graph()
    graph.parse('../results/final_rdf_complex.ttl', format='turtle')
    ontology_root = 'http://www.semanticweb.org/andreas/ontologies/2021/9/project_tourism_complex#'
    tourism_intelligence_ontology = Namespace(ontology_root)
    graph.bind("tio", tourism_intelligence_ontology)

comment_cq2 = '# CQ2: How many accommodations are available at a specific touristic point? 242'
query_cq2 = """
SELECT DISTINCT ?acc_num
WHERE {
    ?s rdf:type tio:Hotels_Statistics .
    ?s tio:touristic_point tio:Benidorm .
    ?s tio:month tio:8 .
    ?s tio:year tio:2021 .
    ?s tio:establishments ?acc_num .
}
"""

comment_cq14 = '# CQ14: How many tourists come from Germany in any given month? 547054 (for August,2021)'
query_cq14 = """
SELECT DISTINCT ?total_tourists (SUM(?t) AS ?total_tourists)
WHERE {
        ?s tio:country_of_origin ?country FILTER ( str(?country) = "Alemania" ) .
        ?s tio:month tio:8 .
        ?s tio:year tio:2021 .
        ?s tio:tourists ?t .
}
"""

# query graph
comment = comment_cq14
query = query_cq14
query_result = graph.query(query)
for row in query_result:
    print(f"{comment}{query}Answer: {row}")
