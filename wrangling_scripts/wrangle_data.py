import pandas as pd
import plotly.graph_objs as go

# TODO: Scroll down to line 157 and set up a fifth visualization for the data dashboard
## TO DO ROUND TO 1 DECIMAL. FUNCTION THE API TO RETURN 4 DATA FRAMES
def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

  # first chart plots arable land from 1990 to 2015 in top 10 economies 
  # as a line chart


# second chart plots ararble land for 2015 as a bar chart    
    graph_one = []
    df = pd.read_csv('data/scorehome.csv')
    
    df.sort_values('ATTP', ascending=False, inplace=True)
    df = df.head(5)


    graph_one.append(
      go.Bar(
      x = df.team.tolist(),
      y = df.ATTP.tolist(),
      text=df.ATTP.tolist(),
      textposition = 'auto',
      marker=dict(
        color=['rgba(34,139,34,0.8)','rgba(204,204,204,1)', 
               'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(204,204,204,1)'],
        line=dict(
        color='rgb(8,48,107)',
        width=1.5),
            ),
        opacity=0.8
            ))
            
        

    layout_one = dict(title = 'STR scores when at Home',
                xaxis = dict(title = 'Team',),
                yaxis = dict(title = 'Ave points per round'),
                )
      
    graph_two = []
    df = pd.read_csv('data/scoreaway.csv')
    
    df.sort_values('ATTP', ascending=False, inplace=True)
    df = df.head(5)  
      
    graph_two.append(
      go.Bar(
      x = df.team.tolist(),
      y = df.ATTP.tolist(),
      text=df.ATTP.tolist(),
      textposition = 'auto',
      marker=dict(
        color=['rgba(34,139,34,0.8)','rgba(204,204,204,1)', 
               'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(204,204,204,1)'],
        line=dict(
        color='rgb(8,48,107)',
        width=1.5),
            ),
        opacity=0.8
            ))
            
        

    layout_two = dict(title = 'STR scores when Away',
                xaxis = dict(title = 'Team',),
                yaxis = dict(title = 'Ave points per round'),
                )
          
    graph_three = []
    df = pd.read_csv('data/letinhome.csv')
    
    df.sort_values('ATTP', ascending=False, inplace=True)
    df = df.head(5)  
      
    graph_three.append(
      go.Bar(
      x = df.opponent.tolist(),
      y = df.ATTP.tolist(),
      text=df.ATTP.tolist(),
      textposition = 'auto',
      marker=dict(
        color=['rgba(203, 65, 84,0.8)','rgba(204,204,204,1)', 
               'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(204,204,204,1)'],
        line=dict(
        color='rgb(8,48,107)',
        width=1.5),
            ),
        opacity=0.8
            ))
            
        

    layout_three = dict(title = 'STR scores against when Home',
                xaxis = dict(title = 'Team',),
                yaxis = dict(title = 'Ave points per round'),
                )
    
          
    graph_four = []
    df = pd.read_csv('data/letinaway.csv')
    
    df.sort_values('ATTP', ascending=False, inplace=True)
    df = df.head(5)  
      
    graph_four.append(
      go.Bar(
      x = df.opponent.tolist(),
      y = df.ATTP.tolist(),
      text=df.ATTP.tolist(),
      textposition = 'auto',
      marker=dict(
        color=['rgba(203, 65, 84,0.8)','rgba(204,204,204,1)', 
               'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(204,204,204,1)'],
        line=dict(
        color='rgb(8,48,107)',
        width=1.5),
            ),
        opacity=0.8
            ))
            
        

    layout_four = dict(title = 'STR scores against when Away',
                xaxis = dict(title = 'Team',),
                yaxis = dict(title = 'Ave points per round'),
                )
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures