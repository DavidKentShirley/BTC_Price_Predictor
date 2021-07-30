# Bitcoin Price Predictor





# Project Overview

This project is using three different methods to try and predict the future price of Bitcoin. The first model was created using Facebook Prophet, the second with linear regression and the last was using keras LSTM.



# Business Overview

Predicting the future price of Bitcoin. Building a model that would be able to predict the future price of BTC and possibly other cryptos as well. The main goal of this model is to see if it is possible to make such predictions and how accurate you could get them using a few different methods (Listed Above). 

The main audience for this project/model would be investors and people who use BTC on a day to day bases when making transaction. Having the ability to know what the price of BTC would be when investing or making transactions with BTC would extremally helpful. 

The value that a model like this would bring to the people who use it would be priceless because it would enable them to make a lot of money and very safe and secure BTC purchases. If this model can also be used for other cryptos or even stocks than the value would be limitless.



# Process



![](https://i.imgur.com/mH1rGN0.png)



1. The first step is to get the data needed to train and test the models. This data is coming from the Yahoo Finance API and some information that it comes with is Open, Close, Volume, High and Low. These are are related to the price and stocks. For this project the data that was gathered was the BTC prices from 1/1/17 - 7/27/21.
2. After the data has been gathered the next step is to look through it find any missing/null values remove them and do some feature engineering/formatting for each model that is going to be used. 
3. Making a base model to go off of / First Simple Model. In this case an easy model to make and have as a good starting point was the Facebook Prophet model and forecast for the future price of BTC.
4. Making more models in order to find one that would have good results. Trying three different methods in order to see if any would yield viable results. Linear Regression, Neural Network, and Prophet. 
5. The final phase of this project is to evaluate the models to see which one performed the best and to deploy that model so others can see/use it to their liking. 

# Models

### FB Prophet 

![](https://i.imgur.com/3HKG0xQ.png)

The first model which was the FB Prophet model had some interesting results.

* RMSE: 2,523.23
* The model preformed very well but its future predictions seemed really high. 

### Linear Regression

ADD

### LSTM

ADD

* RMSE: 3,456.72
* This model performed very well and has some really good future predictions that didn't just skyrocket the price to 100k.

# Conclusion

The best overall model was the LSTM model that had a good RMSE and future predictions that made sense/looked better than the other models that were made. <br>

The overall question of weather being able to predict the future price of BTC is hard to answer. It  is not easy to predict something that has so many external factors that affects it's price but if we were able to feed data through it and come up with a data flow of news events twitter feeds and tons of other features, we might be able to get closer to the actual future value of BTC.
