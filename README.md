# Predicting used Car prices using Deep Learning

## Table of Contents

* [General Info](#general-info)
* [Technologies](#technologies)
* [Looking at the big picture](#looking-at-the-big-picture)
* [Get the data](#get-the-data)
* [Discover and Visualize the data to gain insight](#discover-and-visualize-the-data-to-gain-insight)


## General Info
Every Machine Learning project has it's step's so does this. The steps that we will have in this project are:

1. Looking at the big picture:

	In the big picture we frame our problems, define our goals, select the type of learning, decide which tool's we will use and share our related knowledge.
	Usualy we create Machine Learinig Pipelines. What is a ML Pipeline? It is a scheme which gives us a view what type of ML learning we need. This is the 
	fundament of every ML project. If we don't do this part good we will defenitly have a hard time working on this project.

2. Get the data:
	
	We get our data moustly from databases were the client stores it. For educational purposes most common data sources are .csv or .xlsx files. When working
	with real world datasets we have a hard time. Because the real world datasets contain categorical data and missing data. We will discouss this later. In this 
	part we are interested in the .info() and .describe() methods. The .info() method gives us a insight of what type of data can we expect in the dataset. 
	The .describe() method gives us the count, mean, standard deviation and quantile parameters.

3. Discover and visualize the data to gain insight:
	
	The most insight we can achieve is through visualization. To select the right type of visualization is dependent on the data. But the general roule is to
	keep things simple. Don't overdoit with colors, don't cram the charts.
	The tools for this section are Python library's matplotlib, seaborn, ploty. The second most popular software for data visualization is Tableau. I usuly like
	to combine.

4. Prepare the data for the Machine Learning Algorithm:

	This part includes data preprocessing, scaling and preparing. For the preprocessing part most popular Python library is sklearn. Also the ML algorithm 
	accepts data only in the numpy array so we need to shape it.
	We split our data in this part into:
        
        a) Training set - 80%
		b) Validation set - 10%
		c) Testing set - 10%

5. Select the model and train it:

	As we discused the model selection in the first part we go to work in this part. Here we initialize our neural networks, compile and fit them.

6. Fine-tune your model:

	This part includes experimenting with the hyperparameters such as learning rate, initialization, loss function, activation function.

7. Present your solution:

	We present our solution to our project managers, clients and others. We compare the real and predicted values. Visualize them and make asumptions about them.

8. Lounch, monitor, maintain the system:
	
	We lounch our models inside a web app, mobile app, program. We monitor the and maintain them.

</br>

## Technologies

For this project we will use:

* Python 3.7.7 (https://www.python.org/)
* Jupyter Notebook (https://jupyter.org/)
* Visual Studio Code (https://code.visualstudio.com/)
* TensorFlow 2.1.0 (https://www.tensorflow.org/)
* Git & GitHub (https://github.com/)
* Windows Subsystem for Linux (WSL2) (https://docs.microsoft.com/en-us/windows/wsl/wsl2-index)

</br>

## Looking at the big picture

For this project our goal is to predict used car prices and we will build a prediction model to do this using the TensorFlow Framework. We also have our dataSet which you can find in our source directory or on the kaggle website(// add link).

Next is to select the type of Machine Learning. We said that we have our dataSet that contains the target prices so will use the Supervised learning. 

Our problems are as usual ML projects in the begining are: missing data, categorical data, text data, useless data. We must deal with all of this stuff.

</br>

## Get the data

We will import our data to our Jupyter Notebook from our source directory:

<code>rawData = pd.read_csv('source/autos.csv', <b>encoding = 'iso-8859-1'</b>)</code>

While trying to import our data from the file we had a problem, the method didn't want to read our dataSet so we neded to include another parameter in the method and that is encoding. 
We fixsed our problem by reading a article on StackOverflow(// link)

After fixing this problem we now need to apply the <b>info()</b> and <b>describe()</b> mathods to gain a bit of insight into our data.

Our dataSet consist of:
</br>
<table>
    <tr>
        <th>Name of the column</th>
        <th>Name of the column</th>
        <th>Name of the column</th>
        <th>Name of the column</th>
        <th>Name of the column</th>
    </tr>
    <tr>
        <td>dateCrawled</td>
        <td>name</td>
        <td>seller</td>
        <td>offerType</td>
        <td>price</td>
    </tr>
    <tr>
        <td>abtest</td>
        <td>vehicleType</td>
        <td>yearOfRegistration</td>
        <td>gearbox</td>
        <td>powerPS</td>
    </tr>
    <tr> 
        <td>model</td>
        <td>kilometer</td>
        <td>monthOfRegistration</td>
        <td>fuelType</td>
        <td>brand</td>
    </tr>    
    <tr>     
        <td>notRepairedDamage</td>
        <td>dateCreated</td>
        <td>nrOfPictures</td>
        <td>postalCode</td>
        <td>lastSeen</td>
    </tr>
</table>

</br>

## Discover and Visualize the data to gain insight

To visualize our data we will use the Tableau software. It is the best data visualization tool out there and id does not need much computer power to visualize the data, as it is with Python where some of the visualizations won't even render. This is also the reason why I use it.

We visualized the data using Python and Tableau, you can find the charts inside the visualizations folder, also the Tableau file is inclded. 

As we finish our visualizations part we will select the columns that are important to us. 
And they are:
</br>
<table>
    <tr>
        <th>Name of the column</th>
    </tr>
    <tr>
        <td>price</td>
    </tr>
    <tr>
        <td>vehicleType</td>
    </tr>
    <tr>
        <td>yearOfRegistration</td>
    </tr>
    <tr>
        <td>gearbox</td>
    </tr>
    <tr>
        <td>powerPS</td>
    </tr>
    <tr> 
        <td>model</td>
    </tr>
    <tr>
        <td>kilometer</td>
    </tr>
    <tr>
        <td>fuelType</td>
    </tr>
    <tr>
        <td>brand</td>
    </tr>
    <tr>
        <td>notRepairedDamage</td>
    </tr>
</table>

</br>

## Prepare the data for the Machine Learning Algorithm:

Those are the relevant columns for us and the whole preprocessing phase will be based on them. Next up is to fill the missing values in the dataset. We will start with the most important parameter and that is price. But we can't fill every single row with a specific mean for that model, brand and vehicle Type. Will do that for the Brands that have more then 5000 listings. Our Average prices we have from our Tableau dashboard.

After thinkering for few days with the class that is included in the commit. We finally created a method that works and replaces values with a condition we got it working and we will continue in the following days to use it to modify garbage price values.
This was the biggest problem so far and we fixed it now. 

We have finished cleaning the price column with droping the remaining 6000 columns that had missing "brand, price, vehicleType" values and we could not specify them. Also we will drop the rows who had missing values in the column "vehicleType".

After these modifications we will move on to fill the missing values in the next fields:

<table>
    <tr>
        <th>Column name</th>
        <th>Number of missing values</th>
    </tr>
    <tr>
        <td>vehicleType</td>
        <td>0</td>
    </tr>
    <tr>
        <td>yearOfRegistration</td>
        <td>0</td>
    </tr>
    <tr>
        <td>gearbox</td>
        <td>9.830</td>
    </tr>
    <tr>
        <td>powerPS</td>
        <td>24.415</td>
    </tr>
    <tr>
        <td>fuelType</td>
        <td>15.424</td>
    </tr>
    <tr>
        <td>brand</td>
        <td>0</td>
    </tr>
    <tr>
        <td>notRepairedDamage</td>
        <td>50.072</td>
    </tr>
    <tr>
        <td>price</td>
        <td>0</td>
    </tr>
</table>
</br>


We filled the missing in the power column using our custom imput class, after that we filled the gearbox and notrepaireddamaged columns with the median and we dont have any missing values outside the fueltype, we will fix that in the comming commits
