## Implementation of CUSTOMERS MANAGERS
This part copying given on the practical class architecture with few modification, such as general entity class.

As for streams - see [streams.txt](./streams.txt).

For connector raw data stream were used - see results in [users.txt](./users.txt).

## Implementation of PRODUCTS MANAGEMENT

We generate products with such fields (for more info see [create-product.avsc](./schema/create-product.avsc)):

```
    name - **str**
    category - **str**
    price - **double**
    barcode - **int**
    description - **str**
```

Then create producer and topic **products_raw_data** (see [main.py](./main.py)
and [product_producer.py](./producer/product_producer.py)).
