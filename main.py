import pandas as pd
from plots import Plots

if __name__ == '__main__':

    p = Plots()
    df = pd.read_csv('autos.csv')
    
    # 1) Gráfico de Distribuição de Veículos com base no Ano de Registro
    p.vehicle_distribution_by_register_year(df)
    # 2) Boxplot com a variação da faixa de preço pelo tipo de veículo
    p.range_price_vehicle_type_variation(df)
    # 3) Countplot com a contagem total de veículos à venda conforme o tipo de veículo
    p.count_vehicle_by_type(df)
    # 4) Número de veículos pertencentes a cada marca
    p.vehicle_per_brand(df)
    # 5) Preço médio dos veículos com base no tipo de veículo, bem como no tipo de caixa de câmbio
    p.price_type_and_gearbox(df)
    # 6) Preço médio do veículo por tipo de combustível e tipo de caixa de câmbio
    p.price_type_fuel_and_gearbox(df)
    # 7) Potência média de um veículo por tipo de veículo e tipo de caixa de câmbio
    p.power_vehicle_type_and_gearbox(df)
    # 8) Preço médio de um veículo por marca, bem como tipo de veículo
    p.heatmap_price_vehicle_type_and_brand(df)