#%% #Used for plotting in Jupyter.
import data_helper as dh
import matplotlib.pyplot as plt

def visualize(data):
    # https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html

    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig1, ax1 = plt.subplots()

    g_df = dh.make_business_gdf(data)
    geo_map = dh.make_map_gdf()

    ax1.set_xlim(-65.90, -65.45)
    ax1.set_ylim(18.00, 18.50)

    geo_map.plot(ax=ax1, markersize=5)
    g_df.plot(ax=ax1, linewidth=0.5, edgecolor='black', cmap='hot')
    ax1.axis('off')

    better_results = data[data['rating'] >= 4.5]
    total_ratings = sum(better_results['user_ratings_total'])

    all_types = []
    for t in better_results['types']:
        for sub_type in t.split(','):
            all_types.append(sub_type)
    all_types = Series(all_types)

    fig2, ax2 = plt.subplots()
    ax2.axis('on')

    ax2 = all_types.value_counts().plot(kind='bar')

    color_theme = [
        '#F6F5F6',
        '#92AECE',
        '#8686A4',
        '#99849A',
        '#485260'
    ]

    ratings = better_results.groupby('rating')['name'].nunique()
    fig3, ax3 = plt.subplots()

    fig3 = plt.pie(
        ratings,
        labels=list(better_results.rating.unique()),
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=0.85,
        colors=color_theme
    )

    centre_circle = plt.Circle(
        (0, 0),
        0.70,
        fc='white'
    )

    fig3 = plt.gcf()
    fig3.gca().add_artist(centre_circle)

    fig4, ax4 = plt.subplots()

    best_results = better_results.nlargest(5, 'user_ratings_total')
    total_ratings = sum(best_results['user_ratings_total'])

    # create donut plots
    startingRadius = 0.7 + (0.3 * (len(best_results) - 1))

    for index, row in best_results.iterrows():
        num_ratings = row['user_ratings_total']
        print(startingRadius)
        revisualizeingPie = total_ratings - num_ratings
        donut_sizes = [revisualizeingPie, num_ratings]

        plt.text(0.01, startingRadius + 0.07, row['name'], horizontalalignment='center', verticalalignment='center')
        fig4 = plt.pie(donut_sizes, radius=startingRadius, startangle=90, colors=['#F6F5F6', '#879096'],
                wedgeprops={"edgecolor": "white", 'linewidth': 1})

        startingRadius-=0.3

    # equal ensures pie chart is drawn as a circle (equal aspect ratio)
    # create circle and place onto pie chart
    circle = plt.Circle(xy=(0, 0), radius=0.35, facecolor='white')
    fig4 = plt.gcf()
    fig4.gca().add_artist(circle)

    plt.show()

visualize(data)