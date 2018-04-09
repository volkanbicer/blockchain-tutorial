# blockchain-tutorial
This is a basic block chain created from scratch to understand how blockchain works under the hood.

Features are;
* Chain details
* New transaction
* Mining
* Registering node
* Consensus algorithm


## Getting started
After you've cloned the repository follow below steps.
* Create virtual environment
```
virtualenv -p python3 p3env
```
* Activate environment
```
source p3env/bin/activate
```
* Install dependencies
```
pip install -r requirements.txt
```


## Running
Simply run application

```
python app.py
```

## Usage

* Get chain details
```
curl http://localhost:5000/chain
```
```
{
  "chain": [
    {
      "index": 1,
      "previous_hash": 1,
      "proof": 100,
      "timestamp": 1523260965.462752,
      "transactions": []
    },
    {
      "index": 2,
      "previous_hash": "f55e860d5fbff553ff6f9150fbaa427b3c1ee3306ace419fa54c4bbb966c4eb8",
      "proof": 35293,
      "timestamp": 1523260992.890889,
      "transactions": [
        {
          "amount": 29,
          "recipient": "asdfasdfasdfasdfasdfasdfasd",
          "sender": "zxcvzxvczxcvzxcvzxcvzxcvzxcv"
        },
        {
          "amount": 1,
          "recipient": "200f887da8ec40a7a687e80e5b3560de",
          "sender": "0"
        }
      ]
    }
  ],
  "length": 2
}
```
* Create transaction
```
curl  -X POST \
        -H "Content-Type: application/json" \
        -d '{
         "sender": "d4ee26eee15148ee92c6cd394edd974e",
         "recipient": "someone-other-address",
         "amount": 12
        }'\
        "http://localhost:5000/transactions/new"
```

* Mining
```
curl http://localhost:5000/mine
```
```
{
  "index": 2,
  "message": "New block forged",
  "previous_hash": "f55e860d5fbff553ff6f9150fbaa427b3c1ee3306ace419fa54c4bbb966c4eb8",
  "proof": 35293,
  "transactions": [
    {
      "amount": 29,
      "recipient": "asdfasdfasdfasdfasdfasdfasd",
      "sender": "zxcvzxvczxcvzxcvzxcvzxcvzxcv"
    },
    {
      "amount": 1,
      "recipient": "200f887da8ec40a7a687e80e5b3560de",
      "sender": "0"
    }
  ]
}
```

* Register new node to network
```
curl http://localhost:5000/nodes/register
```

* Resolves any conflicts to ensure a node has the correct chain.
```
curl http://localhost:5000/nodes/resolve
```
