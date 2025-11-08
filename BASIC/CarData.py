Car_data = {
"EV":
    {"maruti":
         {"boleno":{"price" : 700000 , "model":"vx"},
          "scros":{"price" : 799999, "model": "lx"} },
    "hundai": 
        {"verna":{ "price":1200000, "model": "t"},
         "creta":{ "price": 125000, "model": "v"} }         

    },
"desel":
        {"maruti":
                 {"boleno":{"price" : 700000 , "model":"vx"},
                "scros":{"price" : 799999, "model": "lx"} },
        "hundai": 
                {"verna":{ "price":1200000, "model": "t"},
                "creta":{ "price": 125000, "model": "v"} }
    },

 "petrol":
          {"maruti":
                    {"boleno":{"price" : 700000 , "model":"vx"},
                    "scros":{"price" : 799999, "model": "lx"} },
          "hundai": 
                    {"verna":{ "price":1200000, "model": "t"},
                    "creta":{ "price": 125000, "model": "v"}}
}}

k = input("enter a car:")
print(f"this is your {k} variant {Car_data[k]}")

