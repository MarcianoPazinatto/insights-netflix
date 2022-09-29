import pandas as pd
import matplotlib.pyplot as plt
from read_excel import ReadXlsx
import seaborn as sns


class CreateInsights:
    def __init__(self, dataframe):
        self.dataframe = ReadXlsx(dataframe).open_xlsx()

    def drop_duplicates(self, id):
        self.dataframe.drop_duplicates(subset=id, keep=False, inplace=True)
        print(f"Removendo linhas duplicadas com referência no id: {id}.")

    def first_five_rows(self):
        print(f"Primeiras 5 linhas do dataframe: \n{self.dataframe.head()}")

    def df_len(self):
        shape = self.dataframe.shape
        df = str(shape).replace("(", "").replace(")", "").split(",")
        print(f"Tamanho do do dataframe: linhas= {df[0]}, colunas= {df[1].strip()}")

    def dataframe_types(self):
        print(f"Tipos de dados: \n{self.dataframe.dtypes}")

    def movie_genres(self):
        movie_genres = self.dataframe.groupby(['listed_in', ])['listed_in'].count().reset_index(name='count')
        print(f"Total de gêneros:\n  {movie_genres.set_index('listed_in')}")

    def programs_by_country(self):
        print("países com mais de 100 programas na Netflix.")
        dataframe_country = self.dataframe.groupby(['country'])['country'].count().reset_index(name='programs_count')
        countries_with_more_one_hundred_programs = dataframe_country.query("`programs_count` >= 100")
        print(countries_with_more_one_hundred_programs)

    def group_by_year(self):
        self.dataframe["date_added"] = pd.to_datetime(self.dataframe["date_added"])
        self.dataframe['year_added'] = self.dataframe['date_added'].dt.year
        print("\nGêneros e ano de lançamento.\n")
        print(self.dataframe.
              groupby(['year_added', 'listed_in'])['listed_in'].count().reset_index(name='release_count'))

    def types_genres(self):
        colors = ['#3cd6d1', '#de3153']
        types = self.dataframe.groupby(['type', ])['type'].count().reset_index(name='count')
        types = types.set_index('type')
        types.plot.pie(y='count', autopct='%.1f%%', shadow=True, legend='type', figsize=(6, 6), colors=colors)
        plt.show()
        print(plt.title('types_of_show', fontsize=20))

    def top_countries(self):
        dataframe_country = self.dataframe.groupby(['country'])['country'].count().reset_index(name='programs_count')
        top_countries = dataframe_country.query("`programs_count` >= 200")
        sns.barplot(x=top_countries.reset_index()['country'], y=top_countries.reset_index()['programs_count'],
                    hue=top_countries.reset_index()['country'])
        plt.title(' top_countries', fontsize=16)
        plt.xlabel('country', fontsize=16)
        plt.ylabel('programs_count', fontsize=16)
        sns.set(rc={'figure.figsize': (20, 10)})
        plt.show()
        print(plt.xticks(rotation=45))


if __name__ == '__main__':
    insights_netflix = CreateInsights("netflix.xlsx")
    insights_netflix.drop_duplicates("show_id")
    insights_netflix.first_five_rows()
    insights_netflix.df_len()
    insights_netflix.dataframe_types()
    insights_netflix.movie_genres()
    insights_netflix.programs_by_country()
    insights_netflix.group_by_year()
    insights_netflix.types_genres()
    insights_netflix.top_countries()
