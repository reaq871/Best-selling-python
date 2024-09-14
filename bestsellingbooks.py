import streamlit as st
import pandas as pd
import plotly.express as px

books_df=pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title('Best selling books')
st.write('This app analyzes the Amazon top selling books from 2009 to 2022')

st.sidebar.header("Filter Options")
selected_authors = st.sidebar.selectbox("Se;ect Author"["All"]+list(books_df["Authors"].unique()))
selected_year = st.sidebar.selectbox("Select year", ["All"]+list(books_df["Year"].unique()))
selected_genre = st.sidebar.selectbox("Select Genre", ["All"]+list(books_df["Genre"].unique()))
main_rating = st.sidebar.slider("Minimum User Rating", min_value=0.0, max_value=5.0, value=0.1)
max_price = st.sidebar.slider("Maximum Price",0,books_df["Price"].max(),1)

filtered_books.df = books_df.copy()
if selected_authors != "All":
    filtered_books_df = filtered_books_df[filtered_books_df["Author"]==selected_authors]
if selected_year != "ALl":
    filtered_books_df = filtered_books_df[filtered_books_df["Year"]==selected_year]
if selected_genre != "All":
    filtered_books_df = filtered_books_df[(filtered_books_df["Genre"]>=selected_genre)]

filtered_books_df=filtered_books_df[(filtered_books_df["User Rating"]>=min_rating)] & (filtered_books_df["Price" <= max_price])

st.subheader('Summary statistics')
total_books= filtered_books_df.shape[0]
unique_title= books_df['Name'].nunique()
average_rating= books_df['User Rating'].mean()
average_price= books_df['Price'].mean()

col1, col2, col3, col4= st.columns(4)

col1.metric('Average Rating', total_books)
col2.metric('Average Price', unique_title)
col3.metric('Average Rating', f"{average_rating:.2f}")
col4.metric('Average Price', f"${average_price:.2f}")

st.subheader('Dataset review')
st.write(books_df.head())

col1,col2=st.columns(2)

with col1:
    st.header("Top 10 rated titles")
    top_titles=books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.header("Top 10 Authors")
    top_authors=books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")
fig=px.pie(books_df,names='Genre',title='Genre Distribution',color='Genre',color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number of fictional and non fictional books over the years")
size=books_df.groupby(["Year","Genre"]).size().reset_index(name="Counts")
fig=px.bar(size, x="Year", y="Counts,",title="Number of Fictional and Non-Fictional Books", color_discrete_sequence=px.colors.sequential.Plasma,barmode="group")
st.plotly_chart(fig)

st.subheader("Top 15 authors")
top_authors=books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns=['Author','Count']
fig=px.bar(top_authors,x="Count",y="Author",orientation='h',title="Top 15 authors",labels={'Count':'Counts of books published','Author':'Author'},
          color='Count', color_countinous_scale=px.colors.sequential.Plasma)

st.plotly_chart(fig)


st.subheader("filter data by genre")
genre_filter=st.selectbox("Select Genre",books_df['Genre'].unique())
filter_df=books_df[books_df["genre"]==genre_filter]
st.write(filter_df)

st.sidebar.header("Add New Book Data")
with st.sidebar.form("book form"):
    new_name=st.text_input("Enter Author")
    new_user_rating=st.slider("User Rating", min_value=0.0, max_value=5.0, value=0.1)
    new_reviews=st.number_input("Reviews", min_value=0.0, max_value=5.0, step=1.0)
    new_year=st.number_input("Year", min_value=1999, max_value=2024)
    new_genre=st.selectbox("Genre", books.df['Genre'].unique())
    new_price=st.number_input("Price", min_value=0, step=1)
    submit_button=st.form_submit_button(label="Add a new book")

if submit_button:
    new_data={
        "Name": new_name,
        "Author": new_author,
        "Genre": new_genre,
        "Price": new_price,
        "Reviews": new_reviews,
        "Year": new_year,
        "user Rating": new_user_rating
    }
    books_df=pd.concat([pd.DataFrame(new_data, index=[0]), books_df], ignore_index=True)
    books_df.to_csv("bestsellers_with_categories_2022_03_27.csv", index=False)
    st.sidebar.success("New book added succesfully!!!")


st.sidebar.header("Filter Options")
selected_authors=st.sidebar.selectbox("Se;ect Author"["All"]+list(books_df["Authors"].unique()))
selected_year=st.sidebar.selectbox("Select year", ["All"]+list(books_df["Year"].unique()))
selected_genre=st.sidebar.selectbox("Select Genre",["All"]+list(books_df["Genre"].unique()))
main_rating=st.sidebar.slider("Minimum User Rating", min_value=0.0, max_value=5.0, value=0.1)
max_price=st.sidebar.slider("Maximum Price",0,books_df["Price"].max())

filtered_books.df=books_df.copy()
if selected_authors!="All":
    filtered_books_df=filtered_books_df[filtered_books_df["Author"]==selected_authors]
if selected_year!="ALl":
    filtered_books_df=filtered_books_df[filtered_books_df["Year"]==selected_year]
if selected_genre!="All":
    filtered_books_df=filtered_books_df[(filtered_books_df["User Rating"]>=min_rating)  (filtered_books_df["Price"<=max_price])]

