import time
from rdflib import Graph, URIRef, Literal, Namespace, BNode
from rdflib.namespace import SDO, SOSA
import argparse
import sys
from pathlib import Path
from typing import Union
from dq.defined_namespaces import DQAF

__version__ = "0.0.1"


def load_data(path_or_graph: Union[Path, Graph]) -> Graph:
    if isinstance(path_or_graph, Path):
        return Graph().parse(path_or_graph)
    elif isinstance(path_or_graph, Graph):
        return path_or_graph
    else:
        raise ValueError("Could not load data_to_assess: you must supply either a file or an RDF Graph object")


def assessment_01(g: Graph) -> Graph:
    assessment_type = URIRef("http://example.com/assessment/01")
    result_graph = Graph()
    result_graph.bind("dqaf", DQAF)
    target = URIRef("http://example.com/thingWithResult")
    result_bn = BNode()
    graph_length = len(g)

    if graph_length < 2:
        result_graph.add((target, DQAF.hasDQAFResult, result_bn))
        result_graph.add((result_bn, SOSA.observedProperty, assessment_type))
        result_graph.add((result_bn, SDO.value, Literal(0)))
    elif 2 < graph_length < 3:
        result_graph.add((target, DQAF.hasDQAFResult, result_bn))
        result_graph.add((result_bn, SOSA.observedProperty, assessment_type))
        result_graph.add((result_bn, SDO.value, Literal(2)))
    elif graph_length >= 3:
        result_graph.add((target, DQAF.hasDQAFResult, result_bn))
        result_graph.add((result_bn, SOSA.observedProperty, assessment_type))
        result_graph.add((result_bn, SDO.value, Literal(5)))

    return result_graph


def main(args=None):
    if args is None:  # run via entrypoint
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="dq",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-v",
        "--version",
        help="The version and other info for this instancs of BDR DQ",
        action="store_true",
    )

    parser.add_argument(
        "-s",
        "--shacl-validate",
        help="Validate the RDF file with ABIS validation before performing quality assessment",
        action="store_true",
    )

    parser.add_argument(
        "data_to_assess",
        # nargs="?",  # allow 0 or 1 file name as argument
        type=Path,
        help="The ABIS-compliant RDF file, or an RDFLib graph object, to assess",
    )

    args = parser.parse_args(args)

    if args.version:
        print(__version__)
        exit()

    if args.shacl_validate:
        print("Validating input data...")
        # do nothing for now

    # main program
    print("Running BDR-DQ...")
    g = load_data(args.data_to_assess)

    print(assessment_01(g).serialize(format="longturtle"))


if __name__ == "__main__":
    main()
