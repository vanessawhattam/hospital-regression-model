# Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# For regression
import statsmodels.formula.api as smf

#For QQ Plot
import scipy.stats as sts

#Correlation p-values
from scipy.stats import pearsonr

#Regression output
from sklearn.linear_model import LinearRegression

# binning
from scipy.stats import binned_statistic

# Read in the data
hosp_data = pd.read_table("data/calihospital.txt")
hosp_data.dtypes


# Teaching
hosp_data['Teaching'].unique()

# Create dummy variables from the avlbeds_cat
hosp_teaching_dummy = pd.get_dummies(hosp_data['Teaching'], dtype='int')

# Add the dummies into the df
hosp_data = pd.concat([hosp_data, hosp_teaching_dummy], axis=1)

hosp_data.rename(columns={'Small/Rural': 'Small_Rural'}, inplace=True)

# Get the column names
new_column_names = list(hosp_data.columns)
# Replace the last occurrence of 'Teaching' with 'new_teaching_column_name'
new_column_names[-1] = 'Teaching2'

# Assign the modified column names back to the DataFrame
hosp_data.columns = new_column_names

# check to make sure it worked
hosp_data.head()


# DonorType
hosp_data['DonorType'].unique()

# Create dummy variables from the avlbeds_cat
hosp_donor_dummy = pd.get_dummies(hosp_data['DonorType'], dtype='int')

# Add the dummies into the df
hosp_data = pd.concat([hosp_data, hosp_donor_dummy], axis=1)

# check to make sure it worked
hosp_data.head()

# Gender
hosp_data['Gender'].unique()

# Create dummy variables from the avlbeds_cat
hosp_gender_dummy = pd.get_dummies(hosp_data['Gender'], dtype='int')

# Add the dummies into the df
hosp_data = pd.concat([hosp_data, hosp_gender_dummy], axis=1)

# check to make sure it worked
hosp_data.head()

# PositionTitle
hosp_data['PositionTitle'].unique()

# Create dummy variables from PositionTitle
hosp_position_dummy = pd.get_dummies(hosp_data['PositionTitle'], dtype='int')

# Add the dummies into the df
hosp_data = pd.concat([hosp_data, hosp_position_dummy], axis=1)

hosp_data.rename(columns={'Acting Director': 'Acting_Director',
                   'Regional Representative':'Regional_Representative',
                   'Safety Inspection Member':'Safety_Inspection_Member',
                   'State Board Representative': 'State_Board_Representative'}, inplace=True)

# check to make sure it worked
hosp_data.head()

# Compensation
# set our bin intervals
comp_bin_interval = [23000, 46000, 100000, 250000]

# put the Compensation into bins
bin_counts,bin_edges,binnum = binned_statistic(hosp_data['Compensation'], 
                                               hosp_data['Compensation'], 
                                               statistic='count', 
                                               bins=comp_bin_interval)

print(f'bin counts:', bin_counts, '\nbin edges', bin_edges)


# Create labels for the bins
comp_binlabels = ['comp_23k_45k', 'comp_46k_100k', 'comp_100k_250k']

# Add the avlbeds_cat into the main df
compensation_cat = pd.cut(hosp_data['Compensation'], comp_bin_interval, right=False, retbins=False, labels=comp_binlabels)

# make sure it has the right name
compensation_cat.name = 'compensation_cat'

# Take the binning data and add it as a column to the dataframe
hosp_data = hosp_data.join(pd.DataFrame(compensation_cat))

# Create dummy variables from the compensation_cat
hosp_comp_dummy = pd.get_dummies(hosp_data['compensation_cat'], dtype='int')

# Add the dummies into the df
hosp_data = pd.concat([hosp_data, hosp_comp_dummy], axis=1)

# Check it works
hosp_data.head()

# TypeControl
hosp_data['TypeControl'].unique()

# Create dummy variables from TypeControl
hosp_type_dummy = pd.get_dummies(hosp_data['TypeControl'], dtype='int')

# Add the dummies into the df
hosp_data = pd.concat([hosp_data, hosp_type_dummy], axis=1)

hosp_data.rename(columns={'City/County': 'City_County',
                          'Non Profit': 'Non_Profit',
                          'District':'District'}, inplace=True)

# Check to make sure it worked 
hosp_data.head()

# AvlBeds
# range from 12-909 beds; most are within 0-200 beds
# set our bin intervals
bin_interval = [10, 20, 80, 600, 1000]

# put the AvlBeds into bins
bin_counts,bin_edges,binnum = binned_statistic(hosp_data['AvlBeds'], 
                                               hosp_data['AvlBeds'], 
                                               statistic='count', 
                                               bins=bin_interval)

# Create labels for the bins
binlabels = ['beds_10_19', 'beds_20_79', 'beds_80_599', 'beds_600_1000']

# Add the avlbeds_cat into the main df
avlbeds_cat = pd.cut(hosp_data['AvlBeds'], bin_interval, right=False, retbins=False, labels=binlabels)

# make sure it has the right name
avlbeds_cat.name = 'avlbeds_cat'

# Take the binning data and add it as a column to the dataframe
hosp_data = hosp_data.join(pd.DataFrame(avlbeds_cat))

# Create dummy variables from the avlbeds_cat
hosp_avlbed_dummy = pd.get_dummies(hosp_data['avlbeds_cat'], dtype='int')

# Add the dummies into the df
hosp_data = pd.concat([hosp_data, hosp_avlbed_dummy], axis=1)

# check to make sure it worked
hosp_data.head()


# Run the model
operinc_lm = smf.ols('OperInc ~ Teaching2 + Small_Rural + Charity + Alumni + M + F + Acting_Director + Regional_Representative + Safety_Inspection_Member + State_Board_Representative+ comp_23k_45k + comp_46k_100k + comp_100k_250k + City_County + District + Investor + Non_Profit + beds_10_19 + beds_20_79 + beds_80_599 + beds_600_1000', hosp_data).fit()
operinc_lm.summary()

operrev_lm = smf.ols('OperRev ~ Teaching2 + Small_Rural + Charity + Alumni + M + F + Acting_Director + Regional_Representative + Safety_Inspection_Member + State_Board_Representative+ comp_23k_45k + comp_46k_100k + comp_100k_250k + City_County + District + Investor + Non_Profit + beds_10_19 + beds_20_79 + beds_80_599 + beds_600_1000', hosp_data).fit()
operrev_lm.summary()

