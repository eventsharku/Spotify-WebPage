import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Set page config
st.set_page_config(page_title="Spotify Wrapped: Christmas Trends", layout="wide")
st.image("pic.png", use_container_width=True)

# Custom styling for Spotify Wrapped Theme
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Circular+Std:400,700&display=swap');
        body {
            color: white;
            background-color: black;
            font-family: 'Circular Std', sans-serif;
        }
        .sub-title {
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            color: #FFFFFF;
            margin-top: 0;
        }
        .scroll-text {
            font-size: 20px;
            text-align: center;
            color: #1DB954;
            margin-top: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .paragraph {
            font-size: 20px;
            text-align: left;
            color: #FFFFFF;
            margin: 50px auto;
            max-width: 800px;
            line-height: 1.8;
        }
        .main-question {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            color: #FFFFFF;
            margin: 20px auto 30px auto;
        }
        .bullet-points {
            margin: 20px auto;
            max-width: 800px;
            padding: 20px;
            list-style: none; /* Remove default bullets */
        }
        .bullet-points li {
            font-size: 18px;
            color: #FFFFFF;
            margin: 10px 0;
            padding: 10px 15px;
            background: #1DB954; /* Spotify green */
            border-radius: 10px;
            display: flex;
            align-items: center;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        }
        .bullet-points li::before {
            content: "🎵"; /* Add music note emoji as a custom bullet */
            font-size: 20px;
            margin-right: 15px;
            color: #FFFFFF;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Home Page
st.markdown("<div class='sub-title'> 🎧 Welcome to an interactive exploration of how Christmas affects music trends across different countries!</div>", unsafe_allow_html=True)
st.markdown("<div class='scroll-text'>Scroll down to explore more insights on how Christmas impacts music streaming!</div>", unsafe_allow_html=True)

# Paragraph Section
# Main Question Section with Larger Font and Center Alignment
st.markdown(
    """
    <div style="text-align: center; margin: 0 auto; max-width: 800px; margin-top: 100px;">
        <h1 style="font-size: 36px; font-weight: bold; color: #FFFFFF;">
            What does Christmas mean for music trends?
        </h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Paragraph Section with Consistent Width and Fixed Line Breaks
st.markdown(
    """
    <div style="text-align: left; margin: 0 auto; max-width: 800px; font-size: 20px; color: #FFFFFF; line-height: 1.8;">
        Have you ever wondered if our music choices are truly our own—or if they’re subtly shaped by the world around us? 
        Music is deeply personal, yet it doesn’t exist in a vacuum. Our listening habits aren’t just a reflection of our 
        individual tastes; they are constantly influenced by the cultural and socio-political events unfolding around us. 
        This curiosity sparked my exploration—how external forces, like major global events, shape the way we engage with music.
    </div>
    <div style="height: 20px;"></div> <!-- Spacer -->
    <div style="text-align: left; margin: 0 auto; max-width: 800px; font-size: 20px; color: #FFFFFF; line-height: 1.8;">
        Therefore, after pitching the idea to my group partners, we turned our attention to one of the most universally 
        recognized cultural moments: the holiday season. Christmas, in particular, is a time when nostalgia, joy, and 
        festivity are woven into the fabric of everyday life. But does this festive atmosphere actually alter our music 
        preferences? Do people naturally gravitate toward cheerful, high-energy songs during Christmas, or is it an 
        illusion created by tradition and commercial influence?
    </div>
    """,
    unsafe_allow_html=True,
)



# "What We Set Out to Discover" Section
st.markdown(
    """
    <div style="text-align: center; margin: 0 auto; max-width: 800px; margin-top: 100px;">
        <h2 style="font-size: 36px; font-weight: bold; color: #FFFFFF;">
            What We Set Out to Discover
        </h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# Bullet Points Section
st.markdown(
    """
    <ul class='bullet-points'>
        <li>How do music trends differ between Christmas-celebrating and non-Christmas-celebrating countries?</li>
        <li>What emotional tones dominate holiday music listening during Christmas?</li>
        <li>How do audio features vary between holiday playlists across cultures?</li>
    </ul>
    """,
    unsafe_allow_html=True,
)

# Adding Space Before the Image
st.markdown(
    """
    <div style="height: 30px;"></div>
    """,
    unsafe_allow_html=True,
)

# Adding the Image
st.image("christmas.png", use_container_width=True, caption="Spotify Christmas Playlist")

# Adding Space Before the Information
st.markdown(
    """
    <div style="height: 30px;"></div>
    """,
    unsafe_allow_html=True,
)

# Adding the Information Section with Highlighted Country Names
st.markdown(
    """
    <div style="text-align: left; margin: 0 auto; max-width: 800px; font-size: 20px; color: #FFFFFF; line-height: 1.8;">
        In order to isolate the impact of Christmas, we needed a comparison—one that would reveal whether the shift in music 
        behavior is driven by the holiday itself or if it's simply part of broader seasonal patterns. A pairwise analysis of commonly
        streamed songs between countries was performed to select the most comparable pair, ensuring the study’s robustness. By analyzing streaming 
        data from both a Christmas-celebrating country (<span style="color: #1DB954; font-weight: bold;">Estonia</span>) 
        and a non-Christmas-celebrating country (<span style="color: #1DB954; font-weight: bold;">Saudi Arabia</span>), 
        we uncover whether the season truly transforms music consumption—or if our playlists remain untouched by the holiday spirit.
    </div>
    """,
    unsafe_allow_html=True,
)

# Adding Space Before the Methodology Section
st.markdown(
    """
    <div style="height: 30px;"></div> <!-- Spacer -->
    """,
    unsafe_allow_html=True,
)

# Methodology Title
st.markdown(
    """
    <h2 style="text-align: center; font-weight: bold; color: #FFFFFF;">Methodology</h2>
    """,
    unsafe_allow_html=True,
)

# Adding a Video to Streamlit
st.markdown(
    """
    <div style="height: 30px;"></div> <!-- Spacer -->
    """,
    unsafe_allow_html=True,
)

st.video("video.mp4", format="video/mp4")

# Methodology Content with Underlined Hyperlink
st.markdown(
    """
    <div style="text-align: center; margin: 0 auto; max-width: 800px; font-size: 20px; color: #FFFFFF; line-height: 1.8;">
        Primary DataSet: Spotify’s Weekly Top 200 Songs dataset from 
        <a href="https://www.kaggle.com/datasets/brunoalarcon123/top-200-spotify-songs-dataset" target="_blank" style="color: #1DB954; text-decoration: underline; font-weight: bold;">
        Kaggle</a>, covering February 2021 to July 2022. <br><br>
        The primary fields of interest in the study include: track name, artist genre, artist names, week, country, and the 
        Spotify audio features such as valence, loudness, tempo, danceability, and acousticness.
    </div>
    """,
    unsafe_allow_html=True,
)

# Add a spacer for vertical spacing
st.markdown(
    """
    <div style="height: 30px;"></div> <!-- Spacer -->
    """,
    unsafe_allow_html=True,
)

# Paragraph text above the posters
st.markdown(
    """
    <div style="text-align: center; font-size: 32px; font-weight: bold; color: #FFFFFF;">
        The Key Methodology Tests:
    </div>
    """,
    unsafe_allow_html=True,
)

# Add a spacer for vertical spacing
st.markdown(
    """
    <div style="height: 30px;"></div> <!-- Spacer -->
    """,
    unsafe_allow_html=True,
)

# Create columns for horizontal alignment
col1, col2, col3, col4 = st.columns(4)

# Add the posters to each column
with col1:
    st.image("poster1.png", use_container_width=True)
with col2:
    st.image("poster2.png", use_container_width=True)
with col3:
    st.image("poster3.png", use_container_width=True)
with col4:
    st.image("poster4.png", use_container_width=True)

# Add vertical space before the paragraph
st.markdown(
    """
    <div style="height: 30px;"></div> <!-- Spacer -->
    """,
    unsafe_allow_html=True,
)

# Add the paragraph content, centered
st.markdown(
    """
    <div style="text-align: left; margin: 0 auto; max-width: 800px; font-size: 20px; color: #FFFFFF; line-height: 1.8;">
        The methodology for this study combined multiple analytical approaches to explore the influence of Christmas on music trends. 
        AI-based classification was used to identify "Christmassy" songs by analyzing metadata such as song titles and artist genres. 
        Sentiment analysis of song lyrics provided insights into emotional trends, while audio features like valence, energy, 
        and danceability were examined to detect changes in the musical characteristics of popular songs. 
        To quantify the causal impact of Christmas, statistical models such as Difference-in-Differences (DiD) and 
        Regression Discontinuity in Time (RDiT) were applied, comparing trends between a Christmas-celebrating country 
        (<span style="color: #1DB954; font-weight: bold;">Estonia</span>) and a non-Christmas-celebrating country 
        (<span style="color: #1DB954; font-weight: bold;">Saudi Arabia</span>). This combination of techniques ensured 
        a comprehensive understanding of the seasonal impact on music behavior.
    </div>
    """,
    unsafe_allow_html=True,
)

# Add additional space after the paragraph if needed
st.markdown(
    """
    <div style="height: 30px;"></div> <!-- Spacer -->
    """,
    unsafe_allow_html=True,
)


# Add a spacer for vertical spacing before the interactive chart
st.markdown(
    """
    <div style="height: 30px;"></div> <!-- Spacer -->
    """,
    unsafe_allow_html=True,
)

# Load the dataset (ensure the dataset is in the same directory or provide the full path)
@st.cache_data
def load_data():
    file_path = "Songs_Estonia_KSA (1).xlsx"  # Update with correct path if needed
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    df['week'] = pd.to_datetime(df['week'])
    df = df[df['country'].isin(['Estonia', 'Saudi Arabia'])]
    df['is_christmassy'] = df['is_christmassy'].map({True: 1, False: 0})
    return df

data = load_data()

# Country selection
st.sidebar.header('Filter Options')
selected_countries = st.sidebar.multiselect(
    'Select countries:',
    options=data['country'].unique(),
    default=['Estonia', 'Saudi Arabia']
)

# Plotting function
def plot_christmas_songs(data, selected_countries):
    data_filtered = data[data['country'].isin(selected_countries)]
    grouped = data_filtered.groupby(['week', 'country'])['is_christmassy'].mean().reset_index()

    # Define figure size and dimensions
    fig, ax = plt.subplots(figsize=(5, 3), dpi=150)  # Adjust size and resolution
    
    # Set background colors
    fig.patch.set_facecolor('black')  # Figure background
    ax.set_facecolor('black')  # Axes background

    # Plot data
    for country in selected_countries:
        country_data = grouped[grouped['country'] == country]
        ax.plot(country_data['week'], country_data['is_christmassy'] * 100, label=country, linewidth=1.5)

    # Add vertical lines
    ax.axvline(pd.to_datetime('2021-11-01'), color='white', linestyle='--', label='November 2021 (Christmas Period)')
    ax.axvline(pd.to_datetime('2022-01-01'), color='red', linestyle='--', label='January 2022 (Christmas Period)')

    # Customize title, labels, and ticks
    ax.set_title('Graphing the percentage of Christmas songs over time for Estonia and Saudi Arabia',
                 fontsize=10, color='white')
    ax.set_xlabel('Week', fontsize=8, color='white')
    ax.set_ylabel('Percentage of Christmas Songs', fontsize=8, color='white')
    ax.legend(fontsize=6, facecolor='black', edgecolor='white', labelcolor='white')
    ax.tick_params(axis='x', rotation=45, labelsize=6, colors='white')
    ax.tick_params(axis='y', labelsize=6, colors='white')

    plt.tight_layout()
    return fig

# Center the graph within a container
with st.container():
    st.markdown("<div style='text-align: center;'><h2 style='color: white;'>Interactive Chart: Christmas Songs Trend</h2></div>", unsafe_allow_html=True)
    if selected_countries:
        fig = plot_christmas_songs(data, selected_countries)
        st.pyplot(fig)  # Render the resized plot
        st.markdown(
            """
            <div style='font-size: 12px; text-align: center; margin-top: 10px; color: white;'>
            Use the `>` on the top left to expand the sidebar and filter data in the graph.
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.write('Please select at least one country to display the chart.')

# Define the paths to the posters
poster_paths = [
    "2.png",
    "3.png",
    "4.png",
    "5.png",
    "6.png",
    "7.png"
]

# Add a header for the results section
st.markdown("<h2 style='text-align: center; color: white;'>Results</h2>", unsafe_allow_html=True)

# Display posters in a 2x3 grid
# First row
col1, col2, col3 = st.columns(3)
with col1:
    st.image(poster_paths[0], use_container_width=True)
with col2:
    st.image(poster_paths[1], use_container_width=True)
with col3:
    st.image(poster_paths[2], use_container_width=True)

# Second row
col4, col5, col6 = st.columns(3)
with col4:
    st.image(poster_paths[3], use_container_width=True)
with col5:
    st.image(poster_paths[4], use_container_width=True)
with col6:
    st.image(poster_paths[5], use_container_width=True)


# Add the paragraph content, centered
st.markdown(
    """
    <div style="text-align: left; margin: 0 auto; max-width: 800px; font-size: 20px; color: #FFFFFF; line-height: 1.8;">
        This project explored how cultural events like Christmas influence music trends, combining data science techniques with real-world streaming data.
        From analyzing emotional tones to identifying shifts in audio features and streaming behavior, this study highlights how music is not just a personal 
        experience but also a reflection of global cultural moments. The findings show the power of data in uncovering insights about human behavior through music.
    </div>
    """,
    unsafe_allow_html=True,
)

import streamlit as st

# Paragraph content
paragraph = """
Dear Hiring Manager,

Thank you for taking the time to explore this webpage as part of my portfolio. I conducted this research project for one of my computer science classes, inspired by Spotify, its API for developers, and my love for the product. To share my work in a more engaging and entertaining way, I decided to go beyond a traditional research format and create this interactive showcase.

I hope you’ve enjoyed it, and I cannot wait to bring my passion, creativity, and skills to Spotify’s incredible team!

For more details, please click [here] to download the full paper and take a closer look at the research.
"""

# Path to the file
file_path = "Spotify_ResearchPaper.pdf"

# Adding paragraph with download button
with st.container():
    st.markdown("<br><br>", unsafe_allow_html=True)  # Add vertical space
    st.markdown(
        f"<div style='text-align: center;'><p style='color: white; font-size: 16px; line-height: 1.5;'>{paragraph}</p></div>",
        unsafe_allow_html=True,
    )
    # Embed the file download
    with open(file_path, "rb") as file:
        st.download_button(
            label="Download Full Research Paper",
            data=file,
            file_name="Spotify_ResearchPaper.pdf",
            mime="application/pdf",
        )
