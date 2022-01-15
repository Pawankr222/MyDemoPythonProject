### convert two list into a dictonary ###
#first list contains country
Country = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cameroon","Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo, Democratic Republic of the","Congo, Republic of the","Costa Rica","Cote d'Ivoire","Croatia","Cuba","Cyprus","Czechia","Denmark","Djibouti","Dominican Republic","Ecuador","Egypt","El Salvador","","Eritrea","Estonia","Eswatini","","Ethiopia","Fiji","Finland","France","Gabon","Georgia","Germany","Ghana","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iraq","Ireland","Israel","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Laos","Latvia","Lebanon","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Country","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Korea","North Macedonia","Norway","Oman","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Rwanda","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Slovakia","Solomon Islands","Somalia","South Africa","","South Korea","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America","Uruguay","Vanuatu","Vatican City (Holy See)","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]
#Second list contains Capital city
Capital = ["Kabul","Tirana","Algiers","Andorra la Vella","Luanda","Saint John's","Buenos Aires","Yerevan","Canberra","Vienna","Baku","Manama","Dhaka","Bridgetown","Minsk","Brussels","Belmopan","Porto-Novo","Thimphu","Sucre (de jure),","La Paz (seat of government)","Sarajevo","Gaborone","Brasilia","Bandar Seri Begawan","Sofia","Ouagadougou","Gitega","Praia","Yaounde","Ottawa","Bangui","N'Djamena","Santiago","Beijing","Bogotá","Moroni","Kinshasa","Brazzaville","San Jose","Yamoussoukro","Zagreb","Havana","Nicosia","Prague","Copenhagen","Djibouti (city)","Santo Domingo","Quito","Cairo","San Salvador","Oyala (seat of government)","Asmara","Tallinn","Mbabane (administrative),","Lobamba (legislative, royal)","Addis Ababa","Suva","Helsinki","Paris","Libreville","Tbilisi","Berlin","Accra","Saint George's","Guatemala City","Conakry","Bissau","Georgetown","Port-au-Prince","Tegucigalpa","Budapest","Reykjavik","New Delhi","Jakarta","Baghdad","Dublin","Jerusalem","Kingston","Tokyo","Amman","Nur-Sultan","Nairobi","Tarawa","Pristina","Kuwait City","Vientiane","Riga","Beirut","Monrovia","Tripoli","Vaduz","Vilnius","Luxembourg (city)","Capital city","Lilongwe","Kuala Lumpur","Male","Bamako","Valletta","Majuro","Nouakchott","Port Louis","Mexico City","Palikir","Monaco","Ulaanbaatar","Podgorica","Rabat","Maputo","Naypyidaw","Windhoek","Yaren District (de facto)","Kathmandu","Amsterdam","Wellington","Managua","Niamey","Abuja","Pyongyang","Skopje","Oslo","Muscat","Ngerulmud","Jerusalem (East)","Panama City","Port Moresby","Asunción","Lima","Manila","Warsaw","Lisbon","Doha","Bucharest","Kigali","Castries","Kingstown","Apia","San Marino","São Tomé","Riyadh","Dakar","Belgrade","Victoria","Freetown","Bratislava","Honiara","Mogadishu","Pretoria (administrative),","Bloemfontein (judicial)","Seoul","Juba","Madrid","Sri Jayawardenepura Kotte","Khartoum","Paramaribo","Stockholm","Bern","Damascus","Taipei","Dushanbe","Dodoma","Bangkok","Dili","Lomé","Nukuʻalofa","Port of Spain","Tunis","Ankara","Ashgabat","Funafuti","Kampala","Kyiv (also known as Kiev)","Abu Dhabi","London","Washington, D.C.","Montevideo","Port Vila","Vatican City","Caracas","Hanoi","Sana'a","Lusaka","Harare"]
#create a empty dictonary
country_capital_info = {}
#creating country - capital dictonary
country_capital_info = dict(zip(Country,Capital))

country_name = input("Please provide country Name: ")
Capital_city = country_capital_info[country_name]

print (f"Capital city of {country_name} is : {Capital_city}")



