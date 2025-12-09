'''
Homework 8 

Total: 30 points (will be converted to 5 points)

Due Date: Tuesday December 16 by 10:30 am

You are given a file reddit_file.txt corresponding to a directed graph.

You are to read the data into the global variable G that holds a suitable graph
structure and answer the following questions. Please note that I refer to this graph
G in the questions.

Networkx documentation:
https://networkx.org/documentation/stable/reference/index.html

Networkx tutorial:
https://networkx.org/documentation/stable/tutorial.html
'''



def read_data_into_graph():
    '''
    (1 point)

    Parameters: None

    This function reads the content of the file 'reddit_file.txt' and
    populates the directed graph G with this data.

    Returns: None
    '''

    # Assuming that the reddit file contains directed graph x -> y



    

def get_num_of_nodes_edges():
    '''
    (1 point)

    Parameters: None

    This function returns the number of nodes and edges in G.

    Returns: a tuple where the first element is the number of nodes
    in 'G' and the second element is the number of edges in 'G'.
    '''


def get_nodes_with_most_outgoing_edges(N):
    '''
    (6 points)

    Parameter: N, number of top ranked nodes of interest
   
    This function identifies the top N nodes in G, where ranking is by
    the number of outward directed edges.
    
    Returns: a list of tuples, each tuple contains a node identifier
    (nodeid or label) and the count of its outward directed edges.
            The list is sorted by this count in descending order.
    '''

def get_nodes_with_most_incoming_edges(N):
    '''
    (6 points)

    Parameter: N, number of top ranked nodes of interest

    This function identifies the top N nodes in G, where ranking is by the
    number of inward directed edges.
        
    Returns: a list of tuples, each tuple contains a node identifier
    (nodeid or label) and the count of its inward directed edges.
            The list is sorted by this count in descending order.
    '''

 
def get_num_of_connected_components():
    '''
    (3 points)

    Parameters: None

    This function returns the number of connected components present in G.

    Returns: a tuple of two integers. The first is the number of strongly
            connected components and the second is the number of weakly
            connected components.
    '''


def get_nth_largest_strongly_connected_component(N):
    '''
    (5 points)

    Parameters: N, this represents a specific rank.
    1 means the largest connected component in number of nodes,
    2 means the second largest and so on.
    
    The function identifies the Nth largest component out of all the
    strongly connected components in G.
    It then returns the number of nodes, number of edges and the average shortest
    path length within this component.
    
    Returns: a list containing information in the following order for the
                selected component: number of nodes, number of edges, 
                the average shortest path length. 
                If there does not exist an Nth largest member of the strongly
                connected components then return [None, 0, 0]

    '''


def distance(D, N):
    '''
    (5 points)

    Parameter: 
        N: a nodeid (aka node label),
        D: a distance. To clarify, in x --> y --> z, x and z are distance 2 apart
        while x and y are distance 1 apart.
    
        This function returns the set of nodes in G that are at distance D to
        a given node N.
    
    Returns: a set of nodes (nodieid/label) that are at distance D from node N.
            If no such nodes exist, returns an empty set.
    '''


def weakly_connected_components(N):
    '''           
    (2 points)

    Parameters: N, component size (i.e., N is the number of nodes).

    This function returns a list containing SUBGRAPHS, one for each weakly
    connected component in G of size N.
    
    Returns: a list of subgraphs as described above
    '''


