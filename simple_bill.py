import pandas as pd

# बिल का डेटा
def generate_bill():
    print("--- बिल कैलकुलेटर शुरू करें ---")
    
    # खाली लिस्ट
    items = []
    prices = []

    # 3 चीज़ें लेने का लूप
    for i in range(3):
        name = input(f"चीज़ {i+1} का नाम: ")
        price = float(input(f"कीमत: "))
        items.append(name)
        prices.append(price)

    # Pandas का इस्तेमाल करके टेबल (DataFrame) बनाना
    df = pd.DataFrame({'चीज़': items, 'कीमत': prices})

    print("\n--- आपका बिल ---")
    print(df)
    print("\nकुल बिल:", df['कीमत'].sum(), "रुपये")

    # CSV फाइल में सेव करना (ये फाइल तुम्हारे लैपटॉप/फोन में बन जाएगी)
    df.to_csv('my_bill.csv', index=False)
    print("\nबिल 'my_bill.csv' नाम की फाइल में सेव हो गया है!")

# फंक्शन चलाना
generate_bill()
