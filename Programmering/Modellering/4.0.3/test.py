import requests
import pandas as pd
import matplotlib.pyplot as plt

def hent_ssb_data(url, query):
    """Funksjon for å hente data fra SSB API."""
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=query, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Feil ved henting av data: {response.status_code}")
        return None

def forbered_data(data, variabel_navn):
    """Konverterer SSBs respons til en pandas DataFrame."""
    rader = data['dataset']['dimension']['Tid']['category']['index'].keys()
    verdier = data['dataset']['value']
    df = pd.DataFrame(data=verdier, index=rader, columns=[variabel_navn])
    df.index.name = 'År'
    df.reset_index(inplace=True)
    df['År'] = df['År'].astype(int)
    return df

def main():
    # API-endepunkter og spørringer for befolkningsvekst og inflasjon
    url = 'https://data.ssb.no/api/v0/no/table/'
    
    # Eksempel queries (Disse må tilpasses basert på faktiske tabellnummer og variabler fra SSB)
    befolkningsvekst_query = {
        "query": [
            {
                "code": "Region",
                "selection": {
                    "filter": "item",
                    "values": ["0"]  # For hele Norge; tilpass dette basert på behov
                }
            },
            {
                "code": "ContentsCode",
                "selection": {
                    "filter": "item",
                    "values": ["FolkemengdensEndring"]  # Eksempelverdi, endre basert på faktisk kode
                }
            }
        ],
        "response": {
            "format": "json-stat"
        }
    }
    
    inflasjon_query = {
        "query": [
            {
                "code": "ContentsCode",
                "selection": {
                    "filter": "item",
                    "values": ["KPI"]  # Konsumprisindeks, tilpass etter faktisk kode
                }
            }
        ],
        "response": {
            "format": "json-stat"
        }
    }

    # Hent data
    befolkningsvekst_data = hent_ssb_data(url + 'XXX', befolkningsvekst_query)  # Erstatt 'XXX' med faktisk tabell-ID
    inflasjon_data = hent_ssb_data(url + 'YYY', inflasjon_query)  # Erstatt 'YYY' med faktisk tabell-ID

    if befolkningsvekst_data and inflasjon_data:
        # Forbered data
        befolkningsvekst_df = forbered_data(befolkningsvekst_data, 'Befolkningsvekst')
        inflasjon_df = forbered_data(inflasjon_data, 'Inflasjon')
        
        # Kombiner dataframes basert på 'År'
        kombinert_df = pd.merge(befolkningsvekst_df, inflasjon_df, on='År')
        
        # Beregn korrelasjon
        korrelasjon = kombinert_df.corr()
        print("Korrelasjon mellom befolkningsvekst og inflasjon:")
        print(korrelasjon)
        
        # Visualiser data
        plt.figure(figsize=(10, 5))
        plt.plot(kombinert_df['År'], kombinert_df['Befolkningsvekst'], label='Befolkningsvekst')
        plt.plot(kombinert_df['År'], kombinert_df['Inflasjon'], label='Inflasjon', secondary_y=True)
        plt.title('Befolkningsvekst vs. Inflasjon')
        plt.xlabel('År')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    main()
