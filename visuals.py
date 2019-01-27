import numpy as np
import plotly.graph_objs as go
import plotly.offline as offline_py
offline_py.init_notebook_mode(connected=True)

def plot_interactions(articles_by_user):
    trace0 = go.Histogram(
        x = articles_by_user,
        xbins = {
            "start": np.min(articles_by_user),
            "end": np.max(articles_by_user),
            "size": 1
        }
    )


    data = [trace0]

    layout = go.Layout(
        title = "DISTRIBUTION OF HOW MANY ARTICLES <br> A USER INTERACTS WITH ",
        xaxis = {
            "title": "Number of articles",
            "automargin": True,
            "showgrid": True,
            "tick0": 0,
            "dtick": 25,
            "zeroline": False
        },
        
        yaxis = {
            "title": "Number of users",
            "automargin": True,
            "showgrid": True,
        }
        
    )

    fig = go.Figure(data = data, layout = layout)

    offline_py.iplot(fig)

def plot_accuracy_train(train_errs_cum, num_latent_feats, df):
    
    trace0 = go.Scatter(
        x = num_latent_feats,
        y = 1 - np.array(train_errs_cum)/df.shape[0]
    )

    data = [trace0]

    layout = go.Layout(
        title = "Accuracy vs # of Features <br> for Training Data",
        xaxis = {
            "title": "# of Features",
            "automargin": True
        },
        yaxis = {
            "title": "Accuracy",
            "automargin": True
        }
    )

    fig = go.Figure(data = data, layout = layout)

    offline_py.iplot(fig)

def plot_accuracy_test(test_errs_cum, num_latent_feats, df):
    trace0 = go.Scatter(
        x = num_latent_feats,
        y = 1 - np.array(test_errs_cum)/df.shape[0]
    )

    data = [trace0]

    layout = go.Layout(
        title = "Accuracy vs # of Features <br> for Test Data",
        xaxis = {
            "title": "# of Features",
            "automargin": True
        },
        yaxis = {
            "title": "Accuracy",
            "automargin": True
        }
    )

    fig = go.Figure(data = data, layout = layout)

    offline_py.iplot(fig)

def plot_f1_train(train_f1, num_latent_feats):

    trace0 = go.Scatter(
        x = num_latent_feats,
        y = train_f1
    )

    data = [trace0]

    layout = go.Layout(
        title = "F1 Score vs # of Features <br> for Training Data",
        xaxis = {
            "title": "# of Features",
            "automargin": True
        },
        yaxis = {
            "title": "F1 Score",
            "automargin": True
        }
    )

    fig = go.Figure(data = data, layout = layout)

    offline_py.iplot(fig)

def plot_f1_test(test_f1, num_latent_feats):

    trace0 = go.Scatter(
        x = num_latent_feats,
        y = test_f1
    )

    data = [trace0]

    layout = go.Layout(
        title = "F1 Score vs # of Features <br> for Test Data",
        xaxis = {
            "title": "# of Features",
            "automargin": True
        },
        yaxis = {
            "title": "F1 Score",
            "automargin": True
        }
    )

    fig = go.Figure(data = data, layout = layout)

    offline_py.iplot(fig)