def categorize_fares(fares, threshold=12):
    
    for x in fares:
        if x > threshold:
            print(f"This fare {x} is high!")
        else:
            print(f"This fare {x} is low")

sample_fares = [8.60, 5.75, 13.25, 21.21]
categorize_fares(sample_fares)
