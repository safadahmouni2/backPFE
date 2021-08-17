data_distribution = {
    "labels":['محمد عبو  ','قيس سعيد  ', 'عبير موسي', 'راشد الغنوشي','الصافي سعيد','يوسف الشاهد','هشام المشيشي '
  ,'ياسين العياري','سيف الدين المخلوف','فيصل التبيني'],
  "data":[342, 518, 564, 662, 313, 355, 461,499,502,506]
}

topicmodeling={
  "Labels": ['Eating', 'Drinking', 'Sleeping', 'Designing', 'Coding', 'Cycling', 'Running'],
  "data":[
      { 
        "values": [65, 59, 90, 81, 56, 55, 40], 
        "label": 'Series A'
         },
    { 
      "values": [28, 48, 40, 19, 96, 27, 100], 
      "label": 'Series B' 
      }
  ]
}

accuracy=[

  {
    "algo":"Random Forest",
    "acc":0.61,
    "err":0
      },
  {
    "algo":"Naive Bayes",
    "acc":0.58,
    "err":0
      },
  {
    "algo":"Logistic Regression",
    "acc":0.63,
    "err":0
      },
       {
    "algo":"Support Vector Machine",
    "acc":0.65,
    "err":0
      },
       {
    "algo":"Long Short-Term Memory",
    "acc":0.92,
    "err":0
      }
]

comparaison={
   "labels":  ['naive bayes','support vector machine','random forest','logistic regression','long short term memory'],
 "data": [0.58,0.61,0.63,0.65,0.92]
}

persondist = {
"labels":['محمد عبو  ','قيس سعيد  ', 'عبير موسي', 'راشد الغنوشي','الصافي سعيد','يوسف الشاهد','هشام المشيشي ','ياسين العياري  ','سيف الدين المخلوف','فيصل التبيني'],
"data" : [7,11, 12, 14,6,8,10,11,11,11]
}

influencedist={
"labels":['1','2','3','5','6','4','7','8','9','10'],
"data" : [7,11, 12, 14,6,8,10,11,11,11]
}