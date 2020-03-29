import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Plots(object):

    def register_year_histogram(self, df):
        sns.distplot(df['yearOfRegistration'], hist=True)
        plt.xlabel("Ano de Registro")
        plt.show()

    # Crie um Plot com a Distribuição de Veículos com base no Ano de Registro
    def vehicle_distribution_by_register_year(self, df):
        # gráfico de distribuição: apenas uma variável
        sns.distplot(df['yearOfRegistration'], hist=True, color='g')
        plt.xlabel("Ano de Registro")
        plt.ylabel("Densidade")
        plt.show()

    # Variação da faixa de preço pelo tipo de veículo
    def range_price_vehicle_type_variation(self, df):
        sns.set(style="whitegrid")
        sns.boxplot(x="vehicleType", y="price", data=df)
        plt.xlabel("Tipo de Veículo")
        plt.ylabel("Range de Preço")
        plt.title("Análise de Outliers")
        plt.show()

    # Contagem total de veículos à venda conforme o tipo de veículo
    def count_vehicle_by_type(self, df):
        sns.set(style="darkgrid")
        pt = sns.countplot(x="vehicleType", data=df, palette="BuPu")
        plt.xlabel("Tipo de Veículo")
        plt.ylabel("Total de Veículos a Venda")
        plt.title("Contagem total de veículos à venda conforme o tipo de veículo")

        # adicionado valores em cada uma das barras
        for p in pt.patches:
            pt.annotate((p.get_height()), (p.get_x()+0.25, p.get_height()))

        plt.show()

    def vehicle_per_brand(self, df):
        df['brand'].value_counts().sort_values().plot(kind='barh')
        plt.xlabel("Número de Veículo")
        plt.ylabel("Marca")
        plt.title("Veículos por marca")
        plt.show()

        # sns.set_style("whitegrid")
        # sns.catplot(y="brand", data=df, kind="count", palette="Reds_r", height=7, aspect=1.5)

    # Preço médio dos veículos com base no tipo de veículo, bem como no tipo de caixa de câmbio
    def price_type_and_gearbox(self, df):
        sns.set(style="whitegrid")
        sns.catplot(x="vehicleType", y="price", hue="gearbox", data=df, kind="bar",)
        plt.xlabel("Tipo de Veículos")
        plt.ylabel("Preço")
        plt.title("Preço médio dos veículos por tipo de veículo e tipo de caixa de câmbio")
        plt.show()

    # Preço médio do veículo por tipo de combustível e tipo de caixa de câmbio
    def price_type_fuel_and_gearbox(self, df):
        sns.set(style="whitegrid")
        colors = ["#20B2AA", "#008B8B", "#008080"]
        sns.catplot(x="fuelType", y="price", hue="gearbox", data=df, kind="bar", palette=colors)
        plt.xlabel("Tipo de Combustível")
        plt.ylabel("Preço")
        plt.title("Preço médio do veículo por tipo de combustível e tipo de caixa de câmbio")
        plt.show()

    # Potência média de um veículo por tipo de veículo e tipo de caixa de câmbio
    def power_vehicle_type_and_gearbox(self, df):
        sns.set(style="whitegrid")
        colors = ["#FF69B4", "#FF1493", "#C71585"]
        sns.barplot(x="vehicleType", y="powerPS", hue="gearbox", data=df, palette=colors)
        plt.xlabel("Tipo de Veículo")
        plt.ylabel("Potência")
        plt.title("Potência média de um veículo por tipo de veículo e tipo de caixa de câmbio")
        plt.show()

    # Preço médio de um veículo por marca, bem como tipo de veículo
    def heatmap_price_vehicle_type_and_brand(self, df):
        # calculando a média
        df2 = df.copy()
        mean = df2.groupby(['brand', 'vehicleType'])['price'].mean().round(0)

        # adicionando a coluna no dataframe
        df2 = df.set_index(['brand', 'vehicleType'])
        df2['avgPrice'] = mean
        df2 = df2.reset_index()

        # Escolhe os pivôs
        htmap = pd.pivot_table(df2, index='brand', columns='vehicleType', values='avgPrice')

        # Draw a heatmap with the numeric values in each cell
        plt.figure(figsize=(10, 25))
        sns.heatmap(htmap, annot=True, fmt=".0f", cmap="YlGnBu")
        plt.xlabel("Tipo de Veículo")
        plt.ylabel("Marca")
        plt.title("Preço médio de um veículo por marca, bem como tipo de veículo")
        plt.show()
