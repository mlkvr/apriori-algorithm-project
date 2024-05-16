from flask import Flask, request, render_template
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/', methods=['GET', 'POST'])
def index():
    graph_url = None
    if request.method == 'POST':
        file = request.files['file']
        df = pd.read_csv(file)
        
        # Veri setini kontrol edin ve yalnızca 0 ve 1 değerlerinden oluştuğundan emin olun
        df = ensure_binary(df)
        
        rules = apply_apriori(df)
        graph_url = visualize_rules(rules)
    return render_template('index.html', graph_url=graph_url)

def ensure_binary(df):
    """
    Veri setindeki değerlerin yalnızca 0 ve 1 olduğundan emin olur.
    Diğer değerleri 1 olarak kabul eder.
    """
    df = df.applymap(lambda x: 1 if x >= 1 else 0)
    return df

def apply_apriori(df, min_support=0.01):
    # 'Transaction' sütununu çıkarın
    df = df.drop(columns=['Transaction'])
    # Apriori algoritmasını uygulayın
    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    return rules

def visualize_rules(rules):
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='support', y='confidence', size='lift', data=rules)
    plt.title('Apriori Algorithm Results')
    plt.xlabel('Support')
    plt.ylabel('Confidence')
    # Dosya adını oluştur
    graph_filename = 'apriori_results.png'
    graph_filepath = os.path.join(app.config['UPLOAD_FOLDER'], graph_filename)
    plt.savefig(graph_filepath)
    plt.close()
    return graph_filename

if __name__ == '__main__':
    app.run(debug=True)
