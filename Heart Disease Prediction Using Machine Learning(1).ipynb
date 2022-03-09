{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Importing the Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. Importing the Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('heart.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Taking Care of Missing Values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age         0\n",
       "sex         0\n",
       "cp          0\n",
       "trestbps    0\n",
       "chol        0\n",
       "fbs         0\n",
       "restecg     0\n",
       "thalach     0\n",
       "exang       0\n",
       "oldpeak     0\n",
       "slope       0\n",
       "ca          0\n",
       "thal        0\n",
       "target      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4. Taking Care of Duplicate Values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_dup = data.duplicated().any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_dup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = data.drop_duplicates()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_dup = data.duplicated().any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_dup"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5. Data Processing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "cate_val = []\n",
    "cont_val = []\n",
    "for column in data.columns:\n",
    "    if data[column].nunique() <=10:\n",
    "        cate_val.append(column)\n",
    "    else:\n",
    "        cont_val.append(column)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'target']"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cate_val"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['age', 'trestbps', 'chol', 'thalach', 'oldpeak']"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cont_val"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 6. Encoding Categorical Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'target']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cate_val"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 2, 3], dtype=int64)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['cp'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "cate_val.remove('sex')\n",
    "cate_val.remove('target')\n",
    "data = pd.get_dummies(data,columns = cate_val,drop_first=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>trestbps</th>\n",
       "      <th>chol</th>\n",
       "      <th>thalach</th>\n",
       "      <th>oldpeak</th>\n",
       "      <th>target</th>\n",
       "      <th>cp_1</th>\n",
       "      <th>cp_2</th>\n",
       "      <th>cp_3</th>\n",
       "      <th>...</th>\n",
       "      <th>exang_1</th>\n",
       "      <th>slope_1</th>\n",
       "      <th>slope_2</th>\n",
       "      <th>ca_1</th>\n",
       "      <th>ca_2</th>\n",
       "      <th>ca_3</th>\n",
       "      <th>ca_4</th>\n",
       "      <th>thal_1</th>\n",
       "      <th>thal_2</th>\n",
       "      <th>thal_3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>52</td>\n",
       "      <td>1</td>\n",
       "      <td>125</td>\n",
       "      <td>212</td>\n",
       "      <td>168</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>53</td>\n",
       "      <td>1</td>\n",
       "      <td>140</td>\n",
       "      <td>203</td>\n",
       "      <td>155</td>\n",
       "      <td>3.1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>70</td>\n",
       "      <td>1</td>\n",
       "      <td>145</td>\n",
       "      <td>174</td>\n",
       "      <td>125</td>\n",
       "      <td>2.6</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>148</td>\n",
       "      <td>203</td>\n",
       "      <td>161</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>62</td>\n",
       "      <td>0</td>\n",
       "      <td>138</td>\n",
       "      <td>294</td>\n",
       "      <td>106</td>\n",
       "      <td>1.9</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   age  sex  trestbps  chol  thalach  oldpeak  target  cp_1  cp_2  cp_3  ...  \\\n",
       "0   52    1       125   212      168      1.0       0     0     0     0  ...   \n",
       "1   53    1       140   203      155      3.1       0     0     0     0  ...   \n",
       "2   70    1       145   174      125      2.6       0     0     0     0  ...   \n",
       "3   61    1       148   203      161      0.0       0     0     0     0  ...   \n",
       "4   62    0       138   294      106      1.9       0     0     0     0  ...   \n",
       "\n",
       "   exang_1  slope_1  slope_2  ca_1  ca_2  ca_3  ca_4  thal_1  thal_2  thal_3  \n",
       "0        0        0        1     0     1     0     0       0       0       1  \n",
       "1        1        0        0     0     0     0     0       0       0       1  \n",
       "2        1        0        0     0     0     0     0       0       0       1  \n",
       "3        0        0        1     1     0     0     0       0       0       1  \n",
       "4        0        1        0     0     0     1     0       0       1       0  \n",
       "\n",
       "[5 rows x 23 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 7. Feature Scaling"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>trestbps</th>\n",
       "      <th>chol</th>\n",
       "      <th>thalach</th>\n",
       "      <th>oldpeak</th>\n",
       "      <th>target</th>\n",
       "      <th>cp_1</th>\n",
       "      <th>cp_2</th>\n",
       "      <th>cp_3</th>\n",
       "      <th>...</th>\n",
       "      <th>exang_1</th>\n",
       "      <th>slope_1</th>\n",
       "      <th>slope_2</th>\n",
       "      <th>ca_1</th>\n",
       "      <th>ca_2</th>\n",
       "      <th>ca_3</th>\n",
       "      <th>ca_4</th>\n",
       "      <th>thal_1</th>\n",
       "      <th>thal_2</th>\n",
       "      <th>thal_3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>52</td>\n",
       "      <td>1</td>\n",
       "      <td>125</td>\n",
       "      <td>212</td>\n",
       "      <td>168</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>53</td>\n",
       "      <td>1</td>\n",
       "      <td>140</td>\n",
       "      <td>203</td>\n",
       "      <td>155</td>\n",
       "      <td>3.1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>70</td>\n",
       "      <td>1</td>\n",
       "      <td>145</td>\n",
       "      <td>174</td>\n",
       "      <td>125</td>\n",
       "      <td>2.6</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>148</td>\n",
       "      <td>203</td>\n",
       "      <td>161</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>62</td>\n",
       "      <td>0</td>\n",
       "      <td>138</td>\n",
       "      <td>294</td>\n",
       "      <td>106</td>\n",
       "      <td>1.9</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   age  sex  trestbps  chol  thalach  oldpeak  target  cp_1  cp_2  cp_3  ...  \\\n",
       "0   52    1       125   212      168      1.0       0     0     0     0  ...   \n",
       "1   53    1       140   203      155      3.1       0     0     0     0  ...   \n",
       "2   70    1       145   174      125      2.6       0     0     0     0  ...   \n",
       "3   61    1       148   203      161      0.0       0     0     0     0  ...   \n",
       "4   62    0       138   294      106      1.9       0     0     0     0  ...   \n",
       "\n",
       "   exang_1  slope_1  slope_2  ca_1  ca_2  ca_3  ca_4  thal_1  thal_2  thal_3  \n",
       "0        0        0        1     0     1     0     0       0       0       1  \n",
       "1        1        0        0     0     0     0     0       0       0       1  \n",
       "2        1        0        0     0     0     0     0       0       0       1  \n",
       "3        0        0        1     1     0     0     0       0       0       1  \n",
       "4        0        1        0     0     0     1     0       0       1       0  \n",
       "\n",
       "[5 rows x 23 columns]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "st = StandardScaler()\n",
    "data[cont_val] = st.fit_transform(data[cont_val])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>trestbps</th>\n",
       "      <th>chol</th>\n",
       "      <th>thalach</th>\n",
       "      <th>oldpeak</th>\n",
       "      <th>target</th>\n",
       "      <th>cp_1</th>\n",
       "      <th>cp_2</th>\n",
       "      <th>cp_3</th>\n",
       "      <th>...</th>\n",
       "      <th>exang_1</th>\n",
       "      <th>slope_1</th>\n",
       "      <th>slope_2</th>\n",
       "      <th>ca_1</th>\n",
       "      <th>ca_2</th>\n",
       "      <th>ca_3</th>\n",
       "      <th>ca_4</th>\n",
       "      <th>thal_1</th>\n",
       "      <th>thal_2</th>\n",
       "      <th>thal_3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-0.267966</td>\n",
       "      <td>1</td>\n",
       "      <td>-0.376556</td>\n",
       "      <td>-0.667728</td>\n",
       "      <td>0.806035</td>\n",
       "      <td>-0.037124</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-0.157260</td>\n",
       "      <td>1</td>\n",
       "      <td>0.478910</td>\n",
       "      <td>-0.841918</td>\n",
       "      <td>0.237495</td>\n",
       "      <td>1.773958</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.724733</td>\n",
       "      <td>1</td>\n",
       "      <td>0.764066</td>\n",
       "      <td>-1.403197</td>\n",
       "      <td>-1.074521</td>\n",
       "      <td>1.342748</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.728383</td>\n",
       "      <td>1</td>\n",
       "      <td>0.935159</td>\n",
       "      <td>-0.841918</td>\n",
       "      <td>0.499898</td>\n",
       "      <td>-0.899544</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.839089</td>\n",
       "      <td>0</td>\n",
       "      <td>0.364848</td>\n",
       "      <td>0.919336</td>\n",
       "      <td>-1.905464</td>\n",
       "      <td>0.739054</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        age  sex  trestbps      chol   thalach   oldpeak  target  cp_1  cp_2  \\\n",
       "0 -0.267966    1 -0.376556 -0.667728  0.806035 -0.037124       0     0     0   \n",
       "1 -0.157260    1  0.478910 -0.841918  0.237495  1.773958       0     0     0   \n",
       "2  1.724733    1  0.764066 -1.403197 -1.074521  1.342748       0     0     0   \n",
       "3  0.728383    1  0.935159 -0.841918  0.499898 -0.899544       0     0     0   \n",
       "4  0.839089    0  0.364848  0.919336 -1.905464  0.739054       0     0     0   \n",
       "\n",
       "   cp_3  ...  exang_1  slope_1  slope_2  ca_1  ca_2  ca_3  ca_4  thal_1  \\\n",
       "0     0  ...        0        0        1     0     1     0     0       0   \n",
       "1     0  ...        1        0        0     0     0     0     0       0   \n",
       "2     0  ...        1        0        0     0     0     0     0       0   \n",
       "3     0  ...        0        0        1     1     0     0     0       0   \n",
       "4     0  ...        0        1        0     0     0     1     0       0   \n",
       "\n",
       "   thal_2  thal_3  \n",
       "0       0       1  \n",
       "1       0       1  \n",
       "2       0       1  \n",
       "3       0       1  \n",
       "4       1       0  \n",
       "\n",
       "[5 rows x 23 columns]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 8. Splitting The Dataset Into The Training Set And Test Set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = data.drop('target',axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = data['target']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,\n",
    "                                               random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "245    1\n",
       "349    0\n",
       "135    0\n",
       "389    1\n",
       "66     1\n",
       "      ..\n",
       "402    1\n",
       "123    1\n",
       "739    0\n",
       "274    1\n",
       "256    1\n",
       "Name: target, Length: 61, dtype: int64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 9. Logistic Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>trestbps</th>\n",
       "      <th>chol</th>\n",
       "      <th>thalach</th>\n",
       "      <th>oldpeak</th>\n",
       "      <th>target</th>\n",
       "      <th>cp_1</th>\n",
       "      <th>cp_2</th>\n",
       "      <th>cp_3</th>\n",
       "      <th>...</th>\n",
       "      <th>exang_1</th>\n",
       "      <th>slope_1</th>\n",
       "      <th>slope_2</th>\n",
       "      <th>ca_1</th>\n",
       "      <th>ca_2</th>\n",
       "      <th>ca_3</th>\n",
       "      <th>ca_4</th>\n",
       "      <th>thal_1</th>\n",
       "      <th>thal_2</th>\n",
       "      <th>thal_3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-0.267966</td>\n",
       "      <td>1</td>\n",
       "      <td>-0.376556</td>\n",
       "      <td>-0.667728</td>\n",
       "      <td>0.806035</td>\n",
       "      <td>-0.037124</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-0.157260</td>\n",
       "      <td>1</td>\n",
       "      <td>0.478910</td>\n",
       "      <td>-0.841918</td>\n",
       "      <td>0.237495</td>\n",
       "      <td>1.773958</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.724733</td>\n",
       "      <td>1</td>\n",
       "      <td>0.764066</td>\n",
       "      <td>-1.403197</td>\n",
       "      <td>-1.074521</td>\n",
       "      <td>1.342748</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.728383</td>\n",
       "      <td>1</td>\n",
       "      <td>0.935159</td>\n",
       "      <td>-0.841918</td>\n",
       "      <td>0.499898</td>\n",
       "      <td>-0.899544</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.839089</td>\n",
       "      <td>0</td>\n",
       "      <td>0.364848</td>\n",
       "      <td>0.919336</td>\n",
       "      <td>-1.905464</td>\n",
       "      <td>0.739054</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        age  sex  trestbps      chol   thalach   oldpeak  target  cp_1  cp_2  \\\n",
       "0 -0.267966    1 -0.376556 -0.667728  0.806035 -0.037124       0     0     0   \n",
       "1 -0.157260    1  0.478910 -0.841918  0.237495  1.773958       0     0     0   \n",
       "2  1.724733    1  0.764066 -1.403197 -1.074521  1.342748       0     0     0   \n",
       "3  0.728383    1  0.935159 -0.841918  0.499898 -0.899544       0     0     0   \n",
       "4  0.839089    0  0.364848  0.919336 -1.905464  0.739054       0     0     0   \n",
       "\n",
       "   cp_3  ...  exang_1  slope_1  slope_2  ca_1  ca_2  ca_3  ca_4  thal_1  \\\n",
       "0     0  ...        0        0        1     0     1     0     0       0   \n",
       "1     0  ...        1        0        0     0     0     0     0       0   \n",
       "2     0  ...        1        0        0     0     0     0     0       0   \n",
       "3     0  ...        0        0        1     1     0     0     0       0   \n",
       "4     0  ...        0        1        0     0     0     1     0       0   \n",
       "\n",
       "   thal_2  thal_3  \n",
       "0       0       1  \n",
       "1       0       1  \n",
       "2       0       1  \n",
       "3       0       1  \n",
       "4       1       0  \n",
       "\n",
       "[5 rows x 23 columns]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression()"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "log = LogisticRegression()\n",
    "log.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred1 = log.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7868852459016393"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test,y_pred1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 10. SVC"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import svm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "svm = svm.SVC()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SVC()"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "svm.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred2 = svm.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8032786885245902"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test,y_pred2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 11. KNeighbors Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "knn = KNeighborsClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsClassifier()"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred3=knn.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7377049180327869"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test,y_pred3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "score = []\n",
    "\n",
    "for k in range(1,40):\n",
    "    knn=KNeighborsClassifier(n_neighbors=k)\n",
    "    knn.fit(X_train,y_train)\n",
    "    y_pred=knn.predict(X_test)\n",
    "    score.append(accuracy_score(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0.7213114754098361,\n",
       " 0.8032786885245902,\n",
       " 0.7049180327868853,\n",
       " 0.7049180327868853,\n",
       " 0.7377049180327869,\n",
       " 0.8032786885245902,\n",
       " 0.7868852459016393,\n",
       " 0.8032786885245902,\n",
       " 0.7704918032786885,\n",
       " 0.7540983606557377,\n",
       " 0.7704918032786885,\n",
       " 0.7540983606557377,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7540983606557377,\n",
       " 0.7704918032786885,\n",
       " 0.7540983606557377,\n",
       " 0.7540983606557377,\n",
       " 0.7377049180327869,\n",
       " 0.7540983606557377,\n",
       " 0.7377049180327869,\n",
       " 0.7213114754098361,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7213114754098361,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869,\n",
       " 0.7377049180327869]"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(score)\n",
    "plt.xlabel(\"K Value\")\n",
    "plt.ylabel(\"Acc\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8032786885245902"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn=KNeighborsClassifier(n_neighbors=2)\n",
    "knn.fit(X_train,y_train)\n",
    "y_pred=knn.predict(X_test)\n",
    "accuracy_score(y_test,y_pred)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Non-Linear ML Algorithms"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('heart.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = data.drop_duplicates()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = data.drop('target',axis=1)\n",
    "y=data['target']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,\n",
    "                                                random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 12. Decision Tree Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "dt = DecisionTreeClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier()"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dt.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred4= dt.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7377049180327869"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test,y_pred4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 13. Random Forest Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "rf = RandomForestClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier()"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred5= rf.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.819672131147541"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test,y_pred5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 14. Gradient Boosting Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import GradientBoostingClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "gbc = GradientBoostingClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GradientBoostingClassifier()"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gbc.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred6 = gbc.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8032786885245902"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test,y_pred6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "final_data = pd.DataFrame({'Models':['LR','SVM','KNN','DT','RF','GB'],\n",
    "                          'ACC':[accuracy_score(y_test,y_pred1)*100,\n",
    "                                accuracy_score(y_test,y_pred2)*100,\n",
    "                                accuracy_score(y_test,y_pred3)*100,\n",
    "                                accuracy_score(y_test,y_pred4)*100,\n",
    "                                accuracy_score(y_test,y_pred5)*100,\n",
    "                                accuracy_score(y_test,y_pred6)*100]})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Models</th>\n",
       "      <th>ACC</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>LR</td>\n",
       "      <td>78.688525</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>SVM</td>\n",
       "      <td>80.327869</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>KNN</td>\n",
       "      <td>73.770492</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>DT</td>\n",
       "      <td>73.770492</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>RF</td>\n",
       "      <td>81.967213</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>GB</td>\n",
       "      <td>80.327869</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Models        ACC\n",
       "0     LR  78.688525\n",
       "1    SVM  80.327869\n",
       "2    KNN  73.770492\n",
       "3     DT  73.770492\n",
       "4     RF  81.967213\n",
       "5     GB  80.327869"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Models', ylabel='ACC'>"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(final_data['Models'],final_data['ACC'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "X=data.drop('target',axis=1)\n",
    "y=data['target']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier()"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf = RandomForestClassifier()\n",
    "rf.fit(X,y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 15. Prediction on New Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "new_data = pd.DataFrame({\n",
    "    'age':52,\n",
    "    'sex':1,\n",
    "    'cp':0,\n",
    "    'trestbps':125,\n",
    "    'chol':212,\n",
    "    'fbs':0,\n",
    "    'restecg':1,\n",
    "    'thalach':168,\n",
    "    'exang':0,\n",
    "    'oldpeak':1.0,\n",
    "     'slope':2,\n",
    "    'ca':2,\n",
    "    'thal':3,    \n",
    "},index=[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>cp</th>\n",
       "      <th>trestbps</th>\n",
       "      <th>chol</th>\n",
       "      <th>fbs</th>\n",
       "      <th>restecg</th>\n",
       "      <th>thalach</th>\n",
       "      <th>exang</th>\n",
       "      <th>oldpeak</th>\n",
       "      <th>slope</th>\n",
       "      <th>ca</th>\n",
       "      <th>thal</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>52</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>125</td>\n",
       "      <td>212</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>168</td>\n",
       "      <td>0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  \\\n",
       "0   52    1   0       125   212    0        1      168      0      1.0      2   \n",
       "\n",
       "   ca  thal  \n",
       "0   2     3  "
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No Disease\n"
     ]
    }
   ],
   "source": [
    "p = rf.predict(new_data)\n",
    "if p[0]==0:\n",
    "    print(\"No Disease\")\n",
    "else:\n",
    "    print(\"Disease\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 16. Save Model Using Joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['model_joblib_heart']"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "joblib.dump(rf,'model_joblib_heart')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = joblib.load('model_joblib_heart')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0], dtype=int64)"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict(new_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>cp</th>\n",
       "      <th>trestbps</th>\n",
       "      <th>chol</th>\n",
       "      <th>fbs</th>\n",
       "      <th>restecg</th>\n",
       "      <th>thalach</th>\n",
       "      <th>exang</th>\n",
       "      <th>oldpeak</th>\n",
       "      <th>slope</th>\n",
       "      <th>ca</th>\n",
       "      <th>thal</th>\n",
       "      <th>target</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>723</th>\n",
       "      <td>68</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>120</td>\n",
       "      <td>211</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>115</td>\n",
       "      <td>0</td>\n",
       "      <td>1.5</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>733</th>\n",
       "      <td>44</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>108</td>\n",
       "      <td>141</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>175</td>\n",
       "      <td>0</td>\n",
       "      <td>0.6</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>739</th>\n",
       "      <td>52</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>128</td>\n",
       "      <td>255</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>161</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>843</th>\n",
       "      <td>59</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>160</td>\n",
       "      <td>273</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>125</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>878</th>\n",
       "      <td>54</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>120</td>\n",
       "      <td>188</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>113</td>\n",
       "      <td>0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  \\\n",
       "723   68    0   2       120   211    0        0      115      0      1.5   \n",
       "733   44    0   2       108   141    0        1      175      0      0.6   \n",
       "739   52    1   0       128   255    0        1      161      1      0.0   \n",
       "843   59    1   3       160   273    0        0      125      0      0.0   \n",
       "878   54    1   0       120   188    0        1      113      0      1.4   \n",
       "\n",
       "     slope  ca  thal  target  \n",
       "723      1   0     2       1  \n",
       "733      1   0     2       1  \n",
       "739      2   1     3       0  \n",
       "843      2   0     2       0  \n",
       "878      1   1     3       0  "
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### GUI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "import joblib\n",
    "import numpy as np\n",
    "from sklearn import *\n",
    "def show_entry_fields():\n",
    "    p1=int(e1.get())\n",
    "    p2=int(e2.get())\n",
    "    p3=int(e3.get())\n",
    "    p4=int(e4.get())\n",
    "    p5=int(e5.get())\n",
    "    p6=int(e6.get())\n",
    "    p7=int(e7.get())\n",
    "    p8=int(e8.get())\n",
    "    p9=int(e9.get())\n",
    "    p10=float(e10.get())\n",
    "    p11=int(e11.get())\n",
    "    p12=int(e12.get())\n",
    "    p13=int(e13.get())\n",
    "    model = joblib.load('model_joblib_heart')\n",
    "    result=model.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p8,p10,p11,p12,p13]])\n",
    "    \n",
    "    if result == 0:\n",
    "        Label(master, text=\"No Heart Disease\").grid(row=31)\n",
    "    else:\n",
    "        Label(master, text=\"Possibility of Heart Disease\").grid(row=31)\n",
    "    \n",
    "    \n",
    "master = Tk()\n",
    "master.title(\"Heart Disease Prediction System\")\n",
    "\n",
    "\n",
    "label = Label(master, text = \"Heart Disease Prediction System\"\n",
    "                          , bg = \"black\", fg = \"white\"). \\\n",
    "                               grid(row=0,columnspan=2)\n",
    "\n",
    "\n",
    "Label(master, text=\"Enter Your Age\").grid(row=1)\n",
    "Label(master, text=\"Male Or Female [1/0]\").grid(row=2)\n",
    "Label(master, text=\"Enter Value of CP\").grid(row=3)\n",
    "Label(master, text=\"Enter Value of trestbps\").grid(row=4)\n",
    "Label(master, text=\"Enter Value of chol\").grid(row=5)\n",
    "Label(master, text=\"Enter Value of fbs\").grid(row=6)\n",
    "Label(master, text=\"Enter Value of restecg\").grid(row=7)\n",
    "Label(master, text=\"Enter Value of thalach\").grid(row=8)\n",
    "Label(master, text=\"Enter Value of exang\").grid(row=9)\n",
    "Label(master, text=\"Enter Value of oldpeak\").grid(row=10)\n",
    "Label(master, text=\"Enter Value of slope\").grid(row=11)\n",
    "Label(master, text=\"Enter Value of ca\").grid(row=12)\n",
    "Label(master, text=\"Enter Value of thal\").grid(row=13)\n",
    "\n",
    "\n",
    "\n",
    "e1 = Entry(master)\n",
    "e2 = Entry(master)\n",
    "e3 = Entry(master)\n",
    "e4 = Entry(master)\n",
    "e5 = Entry(master)\n",
    "e6 = Entry(master)\n",
    "e7 = Entry(master)\n",
    "e8 = Entry(master)\n",
    "e9 = Entry(master)\n",
    "e10 = Entry(master)\n",
    "e11 = Entry(master)\n",
    "e12 = Entry(master)\n",
    "e13 = Entry(master)\n",
    "\n",
    "e1.grid(row=1, column=1)\n",
    "e2.grid(row=2, column=1)\n",
    "e3.grid(row=3, column=1)\n",
    "e4.grid(row=4, column=1)\n",
    "e5.grid(row=5, column=1)\n",
    "e6.grid(row=6, column=1)\n",
    "e7.grid(row=7, column=1)\n",
    "e8.grid(row=8, column=1)\n",
    "e9.grid(row=9, column=1)\n",
    "e10.grid(row=10, column=1)\n",
    "e11.grid(row=11, column=1)\n",
    "e12.grid(row=12, column=1)\n",
    "e13.grid(row=13, column=1)\n",
    "\n",
    "\n",
    "\n",
    "Button(master, text='Predict', command=show_entry_fields).grid()\n",
    "\n",
    "mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
