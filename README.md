# zaid-challenge-regression
### dropped columns
url,surfaceofplot,gardenarea,monthlycharges,roomcount,kitchen
### Null values dropped
stateofbuilding,district,province,region
### Null values filled by
constructionyear = mean+ outliers         
bathroomcount = median
garden = 0
fireplace = 0
floodingzone = 'NON_FLOOD_ZONE'
peb= mode
swimmingpool = 0
numberoffacades = median
livingarea = median
terrace = 0
toiletcount = median
furnished = 0

### String covnverted to numerical values by original_ecnoder

region,district,locality,province, stateofbuilding,subtypeofproperty

### choosen features

'bathroomcount','bedroomcount','swimmingpool','subtypeofproperty_encoded',
'numberoffacades','garden','terrace','province_encoded','furnished',
'livingarea','locality_encoded','typeofproperty','region_encoded'


### Modules
DecisionTreeRegressor = 178899.16909224537
GradientBoostingRegressor =162194.11558615518
PolynomialFeatures = 188592.60873178934








