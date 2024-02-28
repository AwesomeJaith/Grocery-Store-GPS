# Grocery Store GPS

Grocery Store GPS is a Python Flask API designed to generate an efficient path for navigating a grocery store according to the items requested by the user.

# Demo

![Grocery Store GPS Demo](https://github.com/AwesomeJaith/Grocery-Store-GPS/blob/main/grocery-store-gps-demo.gif)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AwesomeJaith/Grocery-Store-GPS
   ```
2. Install NPM packages
   ```sh
   npm install
   ```
   
## Usage

### Interactive Testing

You can interactively test the 'map' class by opening and running ```test.ipynb```. In this notebook, you can explore different optimal paths the application generates by modifying the data dictionary in ```test.ipynb```. The data available for grocery items is located in ```woodmans_carpentersville_map_data.json``` under the key ```product_locations```. 

This is an example of what data should look like:
```
data = { "groceries": ["wine", "milk", "cheese", "crackers", "grapes", "spaghetti noodles", "alfredo sauce", "olives"] }
```

Running ```test.ipynb``` will generate an optimal path and provide you with a visualization of that path.


### API Endpoint

You also can send a POST request to: 
```
storeapi.pythonanywhere.com/calculate-optimal-path
```

This endpoint serves you a list with the optimal path through the Woodman's Store in Carpentersville, Illinois given a specific grocery list.

**Input:** "groceries": ["wine", "milk", "cheese", "crackers", "grapes", "spaghetti noodles", "alfredo sauce", "olives"]

**Output:** "optimal_path": [1, 131, 2, 18, 16, 14, 12, 13, 73, 74, 129, 123, 122, 123, 129, 65, 130, 127, 128, 63, 57, 55, 53, 51, 49, 47, 45, 105, 45, 47, 49, 51, 53, 52, 132, 61, 115, 118, 117, 116, 117, 118, 115, 61, 132, 52, 50, 48, 46, 44, 42, 40, 38, 36, 37, 97, 95, 35, 33, 31, 29, 27, 26, 131, 1]

Note: As of now, the deployed API does not provide a meaningful visualization. Enhancing visualization is a feature I hope to include in the future.

## Contributing

Grocery-Store-GPS is an open-source project and we welcome contributions from the community.

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are welcome.

## Motivation

While shopping for groceries one day, I observed a lady rushing around the store to fulfill a delivery order. It struck me that she could potentially optimize her route for efficiency. This inspired me to develop an application that generates an efficient route based on a list of groceries. I also though this would be a fun first project to implement.

## Notes

I would be interested in expanding upon this application and improving the code in the future. Some things I would add are:
* Better visualization/image generation
* An automated way to populate a grocery store map with nodes for the graph
* A usable mobile app

## License

MIT License

Copyright (c) 2024 Jaith Darrah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
