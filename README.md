# zaid-challenge-regression
### dropped columns
url,surfaceofplot,gardenarea,monthlycharges,roomcount,kitchen
### Null values dropped
stateofbuilding,district,province,region
### Null values filled by
constructionyear = mean+ outliers<br/>    
bathroomcount = median<br/>
garden = 0<br/>
fireplace = 0<br/>
floodingzone = 'NON_FLOOD_ZONE'<br/>
peb= mode<br/>
swimmingpool = 0<br/>
numberoffacades = median<br/>
livingarea = median<br/>
terrace = 0<br/>
toiletcount = median<br/>
furnished = 0<br/>

### String covnverted to numerical values by original_ecnoder

region,district,locality,province<br/> 
stateofbuilding,subtypeofproperty

### choosen features

'bathroomcount','bedroomcount','swimmingpool','subtypeofproperty_encoded',<br/>
'numberoffacades','garden','terrace','province_encoded','furnished',<br/>
'livingarea','locality_encoded','typeofproperty','region_encoded'<br/>


### Modules
DecisionTreeRegressor = 178899.16909224537
GradientBoostingRegressor =162194.11558615518
PolynomialFeatures = 188592.60873178934








