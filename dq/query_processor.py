import rdflib


class RDFQueryProcessor:
    def __init__(self, filepath, format="turtle"):
        """
        Initializes the processor with the RDF file.

        Parameters:
        - filepath: The path to the RDF file.
        - format: The format of the RDF file (default: "turtle").
        """
        self.graph = rdflib.Graph()
        self.graph.parse(filepath, format=format)

    def execute_query(self, out_p_uri, aus_st_uri, out_p_value="normal", aus_st_value="Western_Australia"):
        """
        Executes a SPARQL query to find subjects with specific properties.

        Parameters:
        - out_p_uri: The full URI for the out_p property.
        - aus_st_uri: The full URI for the aus_st property.
        - out_p_value: The value for the out_p property to filter by.
        - aus_st_value: The value for the aus_st property to filter by.

        Returns:
        A list of subjects that match the query criteria.
        """
        query = f"""
        PREFIX out_p: <{out_p_uri}>
        

        SELECT ?subject
        WHERE {{
          ?subject out_p:property "{out_p_value}"
                   .
        }}
        """
        return self.graph.query(query)

    def print_results(self, results):
        """
        Prints the subjects from the query results.

        Parameters:
        - results: The results from a SPARQL query execution.
        """
        for row in results:
            print(row.subject)


#Usage :
 #print('Query Execution Test...')
        # Initialize the RDF query processor
 #       rdf_processor = RDFQueryProcessor(result_filename)
 #       label_manager=LabelManager()

        # Replace these URIs with the actual URIs for out_p and aus_st in your RDF data
 #       out_p_uri =  label_manager.get_namespace("outlier_point") #"http://example.org/out_p/"
 #       aus_st_uri = label_manager.get_namespace("australia_state") #"http://example.org/aus_st/"
 #       print(out_p_uri)
 #       print(aus_st_uri)

        # Execute the query
 #       results = rdf_processor.execute_query(out_p_uri, aus_st_uri)

        # Print the results
#        rdf_processor.print_results(results)