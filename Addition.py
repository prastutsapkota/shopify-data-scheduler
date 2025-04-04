import shopify
import pandas as pd
from datetime import datetime

# Your Shopify logic
print("Connecting to Shopify...")

# Simulate data fetch
data = {'order_id': [123, 456], 'total': [100.5, 200.0]}
df = pd.DataFrame(data)

# Save to CSV output
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_path = f"shopify_output_{timestamp}.csv"
df.to_csv(output_path, index=False)

print(f"Data saved to {output_path}")