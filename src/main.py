import requests
import pandas as pd


def standardize(names: list, output_df_name: str ='list_of_normalized_names.csv') -> None:
        """
        Takes a list of compound names and associates each one with the generic name
        The genreic name for each compound is fetched from the pubchem DB
        """

        # Create DF object
        df = pd.DataFrame(names, columns=['input_names'])

        # Initiate an empty list of generic names
        generic_names = []

        # Iterate over input names
        for name in df.input_names:

                # Fetch the list of synonyms from the pubchem DB
                pubchem_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/synonyms/json"

                
                try:
                        # Extract the first synonym, and consider it as a generic one
                        response = requests.get(pubchem_url).json()
                        generic_name = response['InformationList']['Information'][0]['Synonym'][0]
                except:
                        # Use the input name, if the list of synonyms doesn't exist
                        generic_name = name.upper()

                # Add the generic name to the list of generic names
                generic_names.append(generic_name.upper())

        # Add the list of generic names to the DF
        df['normalized_names'] = generic_names

        # Save the DF
        df.to_csv(output_df_name)


if __name__ == "__main__":

    comp_list = ["Adenosine","Adenocard","BG8967","Bivalirudin","BAYT006267","diflucan","ibrutinib","PC-32765", "AA"]
    standardize(comp_list)
