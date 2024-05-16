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
    rules_table = None
    message = None
    if request.method == 'POST':
        if 'file' not in request.files or 'min_support' not in request.form:
            return "Please provide both a file and a minimum support threshold", 400
        
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        
        df = pd.read_csv(file)
        
        # Veri setini kontrol edin ve yalnızca 0 ve 1 değerlerinden oluştuğundan emin olun
        df = ensure_binary(df)
        
        try:
            min_support = float(request.form['min_support'])
        except ValueError:
            return "Invalid minimum support value", 400

        rules, message = apply_apriori(df, min_support)
        if rules is not None:
            graph_url = visualize_rules(rules)
            rules_table = format_rules(rules)
    return render_template('index.html', graph_url=graph_url, rules_table=rules_table, message=message)

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
    if frequent_itemsets.empty:
        return None, "No frequent itemsets found with the given minimum support threshold."
    
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    if rules.empty:
        return None, "No association rules found with the given minimum support threshold."
    
    return rules, None

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

def format_rules(rules):
    """
    Kuralları tablo formatında döndürür ve `confidence` değerine göre azalan şekilde sıralar.
    """
    rules = rules.sort_values(by='confidence', ascending=False)  # `confidence`a göre sıralama
    rules_table = []
    for _, row in rules.iterrows():
        rule = {
            'antecedents': ', '.join(list(row['antecedents'])),
            'consequents': ', '.join(list(row['consequents'])),
            'support': row['support'],
            'confidence': row['confidence'],
            'lift': row['lift']
        }
        rules_table.append(rule)
    return rules_table

if __name__ == '__main__':
    app.run(debug=True)
