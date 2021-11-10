import os
from rdflib import Graph, URIRef, Literal, RDF
import pandas as pd
from mappings import *

# rdflib
graph = Graph()
ontology_root = 'http://www.semanticweb.org/andreas/ontologies/2021/9/project_tourism'
graph.parse('../ontologies/project_tourism_simple.rdf', format='xml')

# input
input_dirs = ['eoh', 'eoac', 'eoal', 'eoap', 'eotr']
# input_dirs = ['eoac', 'eoal', 'eoap', 'eoh', 'eotr']
exclude_dirs = ['output']

for input_dir in input_dirs:
    output_dir = f'{input_dir}/output'

    # loop over all directories in input_dir
    input_dir_path, output_dir_path = '../' + input_dir, '../' + output_dir
    for files_dir in list(filter(lambda val: not val.startswith('.') and val not in exclude_dirs, os.listdir(input_dir_path))):
        files_dir_path = input_dir_path + '/' + files_dir
        output_xls_file_path = output_dir_path + \
            f'/{input_dir}_{files_dir}_all.xls'

        xls_files = []

        # exclude hidden files (e.g. '.DS_Store')
        for file_path in list(filter(lambda val: not val.startswith('.'), os.listdir(files_dir_path))):
            try:
                xls_file = pd.read_excel(files_dir_path + '/' + file_path)
            except:
                print('ERROR at file:' + files_dir_path +
                      '/' + file_path + '\n\n')
            xls_files.append(xls_file)

        df = pd.concat(xls_files, ignore_index=True)
        df.to_excel(output_xls_file_path)

        # transform every row to multiple rdf triples
        for index, row in df.iterrows():

            subject = f'{ontology_root}#{accom_type_mapping[input_dir]}_{class_mapping[files_dir]}_{index}'

            # class
            graph.add((
                URIRef(subject),
                RDF.type,
                URIRef(f'{ontology_root}#{class_mapping[files_dir]}')
            ))

            # data properties
            for prop, type in xsd_type_mapping.items():
                try:
                    value = row[property_mapping[prop]]
                    if not pd.isnull(value):
                        graph.add((
                            URIRef(subject),
                            URIRef(f'{ontology_root}#{prop}'),
                            Literal(value, datatype=type)
                        ))
                except:
                    pass

    graph.serialize(destination='../ontologies/test_eoh_eoac_eoal_eoap_eotr_full.ttl', format='turtle')
