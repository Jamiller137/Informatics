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
import networkx as nx

G = nx.DiGraph()

def read_data_into_graph():
    '''
    (1 point)

    Parameters: None

    This function reads the content of the file 'reddit_file.txt' and
    populates the directed graph G with this data.

    Returns: None
    '''
    global G
    # Assuming that the reddit file contains directed graph x -> y
    # With no errors in the file:

    with open('reddit_file.txt', 'r') as file:
        for line in file:
            parsed = line.split()

            # make sure data makes sense
            assert len(parsed) == 2
            # add edge (automatically adds vertices if DNE)
            G.add_edge(u_of_edge=parsed[0], v_of_edge=parsed[1])

    return None
            
read_data_into_graph()

    


    

def get_num_of_nodes_edges():
    '''
    (1 point)

    Parameters: None

    This function returns the number of nodes and edges in G.

    Returns: a tuple where the first element is the number of nodes
    in 'G' and the second element is the number of edges in 'G'.
    '''
    global G

    return (G.number_of_nodes(), G.number_of_edges())

print(get_num_of_nodes_edges())

def get_nodes_with_most_outgoing_edges(N: int):
    '''
    (6 points)

    Parameter: N, number of top ranked nodes of interest
   
    This function identifies the top N nodes in G, where ranking is by
    the number of outward directed edges.
    
    Returns: a list of tuples, each tuple contains a node identifier
    (nodeid or label) and the count of its outward directed edges.
            The list is sorted by this count in descending order.
    '''
    output = []
    for node in G:
        odeg = G.out_degree(node)
        entry = (node, odeg)

        #first go around automatically append
        if len(output) < N:
            output.append(entry)
            # sort as descending on odeg count
            output = sorted(output, key=lambda x: x[-1], reverse=True)

        elif len(output) >= N:
            if odeg >= output[-1][-1]:
                # remove and add new entry at the end
                output.pop(-1)
                output.append(entry)
                #resort output
                output = sorted(output, key=lambda x: x[-1], reverse=True)

    return output


def get_nodes_with_most_incoming_edges(N: int):
    '''
    (6 points)

    Parameter: N, number of top ranked nodes of interest

    This function identifies the top N nodes in G, where ranking is by the
    number of inward directed edges.
        
    Returns: a list of tuples, each tuple contains a node identifier
    (nodeid or label) and the count of its inward directed edges.
            The list is sorted by this count in descending order.
    '''

    # SAME APPROACH AS OUTGOING EDGES:
    global G
    
    output = []
    for node in G:
        ideg = G.in_degree(node)
        entry = (node, ideg)

        #first go around automatically append
        if len(output) < N:
            output.append(entry)
            # sort as descending on odeg count
            output = sorted(output, key=lambda x: x[-1], reverse=True)

        elif len(output) >= N:
            if ideg >= output[-1][-1]:
                # remove and add new entry at the end
                output.pop(-1)
                output.append(entry)
                #resort output
                output = sorted(output, key=lambda x: x[-1], reverse=True)

    return output


 
def get_num_of_connected_components():
    '''
    (3 points)

    Parameters: None

    This function returns the number of connected components present in G.

    Returns: a tuple of two integers. The first is the number of strongly
            connected components and the second is the number of weakly
            connected components.
    '''
    global G

    return ( nx.number_strongly_connected_components(G), nx.number_weakly_connected_components(G) )



def get_nth_largest_strongly_connected_component(N: int):
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
    global G

    # get list of sorted connected components (uses documentation example)
    comp_list = sorted(nx.strongly_connected_components(G), key=len, reverse=True)

    if len(comp_list) < N:
        raise ValueError(f"There are not enough connected components ( { len(comp_list) } ) for your chosen N = { N } ")

    component = G.subgraph(comp_list[N-1])

    num_nodes = nx.number_of_nodes(component)
    num_edges = nx.number_of_edges(component)
    avg_shortest_path = nx.average_shortest_path_length(component)

    return (num_nodes, num_edges, avg_shortest_path)




def distance(D: int, N):
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

    global G

    result = set()

    node_list = nx.descendants_at_distance(G, N, D)

    for child in node_list:
        result.add(child)

    return result


def weakly_connected_components(N: int):
    '''           
    (2 points)

    Parameters: N, component size (i.e., N is the number of nodes).

    This function returns a list containing SUBGRAPHS, one for each weakly
    connected component in G of size N.
    
    Returns: a list of subgraphs as described above
    '''

    global G

    return [G.subgraph(x) for x in nx.weakly_connected_components(G) if len(x) == N ]

    
