{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "978a5bb4",
   "metadata": {
    "papermill": {
     "duration": 0.01112,
     "end_time": "2023-07-02T17:41:13.586057",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.574937",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**This notebook is an exercise in the [Python](https://www.kaggle.com/learn/python) course.  You can reference the tutorial at [this link](https://www.kaggle.com/colinmorris/hello-python).**\n",
    "\n",
    "---\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5c7c0f60",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:13.605479Z",
     "iopub.status.busy": "2023-07-02T17:41:13.604813Z",
     "iopub.status.idle": "2023-07-02T17:41:13.615521Z",
     "shell.execute_reply": "2023-07-02T17:41:13.614817Z"
    },
    "papermill": {
     "duration": 0.02259,
     "end_time": "2023-07-02T17:41:13.617566",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.594976",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Para adicionar uma célula acima: pressione a tecla 'a' (do inglês, above).\n"
     ]
    }
   ],
   "source": [
    "print(\"Para adicionar uma célula acima: pressione a tecla 'a' (do inglês, above).\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c73bccb3",
   "metadata": {
    "papermill": {
     "duration": 0.008219,
     "end_time": "2023-07-02T17:41:13.634364",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.626145",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Welcome to your first set of Python coding problems.  If this is your first time using Kaggle Notebooks, welcome! \n",
    "\n",
    "Notebooks are composed of blocks (called \"cells\") of text and code. Each of these is editable, though you'll mainly be editing the code cells to answer some questions.\n",
    "\n",
    "To get started, try running the code cell below (by pressing the ► button, or clicking on the cell and pressing ctrl+enter on your keyboard)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4ac73c55",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:13.654599Z",
     "iopub.status.busy": "2023-07-02T17:41:13.653941Z",
     "iopub.status.idle": "2023-07-02T17:41:13.659169Z",
     "shell.execute_reply": "2023-07-02T17:41:13.657858Z"
    },
    "papermill": {
     "duration": 0.017552,
     "end_time": "2023-07-02T17:41:13.661222",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.643670",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Para adicionar uma célula abaixo: pressione a tecla 'b' (do inglês, below).\n"
     ]
    }
   ],
   "source": [
    "print(\"Para adicionar uma célula abaixo: pressione a tecla 'b' (do inglês, below).\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "edcb70b7",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:13.680415Z",
     "iopub.status.busy": "2023-07-02T17:41:13.680095Z",
     "iopub.status.idle": "2023-07-02T17:41:13.685213Z",
     "shell.execute_reply": "2023-07-02T17:41:13.684122Z"
    },
    "papermill": {
     "duration": 0.017569,
     "end_time": "2023-07-02T17:41:13.687651",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.670082",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You've successfully run some Python code\n",
      "Congratulations!\n"
     ]
    }
   ],
   "source": [
    "print(\"You've successfully run some Python code\")\n",
    "print(\"Congratulations!\") \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7bff9a57",
   "metadata": {
    "papermill": {
     "duration": 0.008902,
     "end_time": "2023-07-02T17:41:13.705637",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.696735",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Try adding another line of code in the cell above and re-running it. \n",
    "\n",
    "Now let's get a little fancier:  Add a new code cell by clicking on an existing code cell, hitting the escape key, and then hitting the `a` or `b` key.  The `a` key will add a cell above the current cell, and `b` adds a cell below.\n",
    "\n",
    "Great! Now you know how to use Notebooks.\n",
    "\n",
    "Each hands-on exercise starts by setting up our feedback and code checking mechanism. Run the code cell below to do that. Then you'll be ready to move on to question 0."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e8e3e6f8",
   "metadata": {
    "_kg_hide-input": true,
    "_kg_hide-output": true,
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:13.725818Z",
     "iopub.status.busy": "2023-07-02T17:41:13.725432Z",
     "iopub.status.idle": "2023-07-02T17:41:13.762136Z",
     "shell.execute_reply": "2023-07-02T17:41:13.760882Z"
    },
    "papermill": {
     "duration": 0.049693,
     "end_time": "2023-07-02T17:41:13.764392",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.714699",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Setup complete! You're ready to start question 0.\n"
     ]
    }
   ],
   "source": [
    "from learntools.core import binder; binder.bind(globals())\n",
    "from learntools.python.ex1 import *\n",
    "print(\"Setup complete! You're ready to start question 0.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "73e410a9",
   "metadata": {
    "papermill": {
     "duration": 0.008597,
     "end_time": "2023-07-02T17:41:13.782652",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.774055",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 0.\n",
    "\n",
    "*This is a silly question intended as an introduction to the format we use for hands-on exercises throughout all Kaggle courses.*\n",
    "\n",
    "**What is your favorite color? **\n",
    "\n",
    "To complete this question, create a variable called `color` in the cell below with an appropriate value. The function call `q0.check()` (which we've already provided in the cell below) will check your answer."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ee31859d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:13.802427Z",
     "iopub.status.busy": "2023-07-02T17:41:13.801787Z",
     "iopub.status.idle": "2023-07-02T17:41:13.813128Z",
     "shell.execute_reply": "2023-07-02T17:41:13.811977Z"
    },
    "papermill": {
     "duration": 0.02423,
     "end_time": "2023-07-02T17:41:13.815599",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.791369",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "blue\n"
     ]
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.25, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"0_ExerciseFormatTutorial\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct:</span> What?! You got it right without needing a hint or anything? Drats. Well hey, you should still continue to the next step to get some practice asking for a hint and checking solutions. (Even though you obviously don't need any help here.)"
      ],
      "text/plain": [
       "Correct: What?! You got it right without needing a hint or anything? Drats. Well hey, you should still continue to the next step to get some practice asking for a hint and checking solutions. (Even though you obviously don't need any help here.)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# create a variable called color with an appropriate value on the line below\n",
    "# (Remember, strings in Python must be enclosed in 'single' or \"double\" quotes)\n",
    "color = \"blue\"\n",
    "print(color)\n",
    "\n",
    "# Check your answer\n",
    "q0.check()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d4de073",
   "metadata": {
    "papermill": {
     "duration": 0.00927,
     "end_time": "2023-07-02T17:41:13.834739",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.825469",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Didn't get the right answer? How do you not even know your own favorite color?!\n",
    "\n",
    "Delete the `#` in the line below to make one of the lines run. You can choose between getting a hint or the full answer by choosing which line to remove the `#` from. \n",
    "\n",
    "Removing the `#` is called uncommenting, because it changes that line from a \"comment\" which Python doesn't run to code, which Python does run."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6f3def5e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:13.855568Z",
     "iopub.status.busy": "2023-07-02T17:41:13.854601Z",
     "iopub.status.idle": "2023-07-02T17:41:13.866967Z",
     "shell.execute_reply": "2023-07-02T17:41:13.865845Z"
    },
    "papermill": {
     "duration": 0.02512,
     "end_time": "2023-07-02T17:41:13.869310",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.844190",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 2, \"questionId\": \"0_ExerciseFormatTutorial\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint:</span> Your favorite color rhymes with *glue*."
      ],
      "text/plain": [
       "Hint: Your favorite color rhymes with *glue*."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 2, \"questionId\": \"0_ExerciseFormatTutorial\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> \n",
       "```python\n",
       "color = \"blue\"\n",
       "```"
      ],
      "text/plain": [
       "Solution: \n",
       "```python\n",
       "color = \"blue\"\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "q0.hint()\n",
    "q0.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "734d082f",
   "metadata": {
    "papermill": {
     "duration": 0.010069,
     "end_time": "2023-07-02T17:41:13.889369",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.879300",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "The upcoming questions work the same way. The only thing that will change are the question numbers. For the next question, you'll call `q1.check()`, `q1.hint()`, `q1.solution()`, for question 2, you'll call `q2.check()`, and so on."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fabdd462",
   "metadata": {
    "papermill": {
     "duration": 0.009261,
     "end_time": "2023-07-02T17:41:13.908780",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.899519",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<hr/>\n",
    "\n",
    "# 1.\n",
    "\n",
    "Complete the code below. In case it's helpful, here is the table of available arithmetic operations:\n",
    "\n",
    "\n",
    "\n",
    "| Operator     | Name           | Description                                            |\n",
    "|--------------|----------------|--------------------------------------------------------|\n",
    "| ``a + b``    | Addition       | Sum of ``a`` and ``b``                                 |\n",
    "| ``a - b``    | Subtraction    | Difference of ``a`` and ``b``                          |\n",
    "| ``a * b``    | Multiplication | Product of ``a`` and ``b``                             |\n",
    "| ``a / b``    | True division  | Quotient of ``a`` and ``b``                            |\n",
    "| ``a // b``   | Floor division | Quotient of ``a`` and ``b``, removing fractional parts |\n",
    "| ``a % b``    | Modulus        | Integer remainder after division of ``a`` by ``b``     |\n",
    "| ``a ** b``   | Exponentiation | ``a`` raised to the power of ``b``                     |\n",
    "| ``-a``       | Negation       | The negative of ``a``                                  |\n",
    "\n",
    "<span style=\"display:none\"></span>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "750f9399",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:13.930051Z",
     "iopub.status.busy": "2023-07-02T17:41:13.929406Z",
     "iopub.status.idle": "2023-07-02T17:41:13.938172Z",
     "shell.execute_reply": "2023-07-02T17:41:13.937400Z"
    },
    "papermill": {
     "duration": 0.021723,
     "end_time": "2023-07-02T17:41:13.940161",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.918438",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.25, \"interactionType\": 1, \"questionType\": 1, \"questionId\": \"1_CircleArea\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "pi = 3.14159 # approximate\n",
    "diameter = 3\n",
    "\n",
    "# Create a variable called 'radius' equal to half the diameter\n",
    "radius = diameter/2\n",
    "\n",
    "# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared\n",
    "area = pi*radius**2\n",
    "\n",
    "# Check your answer\n",
    "q1.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "596e97b6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:13.962426Z",
     "iopub.status.busy": "2023-07-02T17:41:13.961850Z",
     "iopub.status.idle": "2023-07-02T17:41:13.974558Z",
     "shell.execute_reply": "2023-07-02T17:41:13.973598Z"
    },
    "papermill": {
     "duration": 0.026504,
     "end_time": "2023-07-02T17:41:13.976513",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.950009",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 1, \"questionId\": \"1_CircleArea\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint:</span> The syntax to raise a to the b'th power is `a ** b`"
      ],
      "text/plain": [
       "Hint: The syntax to raise a to the b'th power is `a ** b`"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 1, \"questionId\": \"1_CircleArea\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> \n",
       "```python\n",
       "radius = diameter / 2\n",
       "area = pi * radius ** 2\n",
       "```"
      ],
      "text/plain": [
       "Solution: \n",
       "```python\n",
       "radius = diameter / 2\n",
       "area = pi * radius ** 2\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Uncomment and run the lines below if you need help.\n",
    "q1.hint()\n",
    "q1.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "244b449d",
   "metadata": {
    "papermill": {
     "duration": 0.011072,
     "end_time": "2023-07-02T17:41:13.999350",
     "exception": false,
     "start_time": "2023-07-02T17:41:13.988278",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<hr/>\n",
    "\n",
    "# 2.\n",
    "\n",
    "Add code to the following cell to swap variables `a` and `b` (so that `a` refers to the object previously referred to by `b` and vice versa)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5e295d13",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:14.023121Z",
     "iopub.status.busy": "2023-07-02T17:41:14.022729Z",
     "iopub.status.idle": "2023-07-02T17:41:14.032121Z",
     "shell.execute_reply": "2023-07-02T17:41:14.031235Z"
    },
    "papermill": {
     "duration": 0.023876,
     "end_time": "2023-07-02T17:41:14.034203",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.010327",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.25, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"2_VariableSwap\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct:</span> \n",
       "\n",
       "The most straightforward solution is to use a third variable to temporarily store one of the old values. e.g.:\n",
       "\n",
       "    tmp = a\n",
       "    a = b\n",
       "    b = tmp\n",
       "\n",
       "If you've read lots of Python code, you might have seen the following trick to swap two variables in one line:\n",
       "\n",
       "    a, b = b, a\n",
       "\n",
       "We'll demystify this bit of Python magic later when we talk about *tuples*."
      ],
      "text/plain": [
       "Correct: \n",
       "\n",
       "The most straightforward solution is to use a third variable to temporarily store one of the old values. e.g.:\n",
       "\n",
       "    tmp = a\n",
       "    a = b\n",
       "    b = tmp\n",
       "\n",
       "If you've read lots of Python code, you might have seen the following trick to swap two variables in one line:\n",
       "\n",
       "    a, b = b, a\n",
       "\n",
       "We'll demystify this bit of Python magic later when we talk about *tuples*."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "########### Setup code - don't touch this part ######################\n",
    "# If you're curious, these are examples of lists. We'll talk about \n",
    "# them in depth a few lessons from now. For now, just know that they're\n",
    "# yet another type of Python object, like int or float.\n",
    "a = [1, 2, 3]\n",
    "b = [3, 2, 1]\n",
    "c = a\n",
    "a = b\n",
    "b = a\n",
    "\n",
    "#a, b = b, a\n",
    "q2.store_original_ids()\n",
    "######################################################################\n",
    "\n",
    "# Your code goes here. Swap the values to which a and b refer.\n",
    "# If you get stuck, you can always uncomment one or both of the lines in\n",
    "# the next cell for a hint, or to peek at the solution.\n",
    "\n",
    "######################################################################\n",
    "\n",
    "# Check your answer\n",
    "q2.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "154ba50f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:14.057602Z",
     "iopub.status.busy": "2023-07-02T17:41:14.056864Z",
     "iopub.status.idle": "2023-07-02T17:41:14.064984Z",
     "shell.execute_reply": "2023-07-02T17:41:14.063885Z"
    },
    "papermill": {
     "duration": 0.021768,
     "end_time": "2023-07-02T17:41:14.066885",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.045117",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 2, \"questionId\": \"2_VariableSwap\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint:</span> Try using a third variable."
      ],
      "text/plain": [
       "Hint: Try using a third variable."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "q2.hint()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a87a9543",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:14.091907Z",
     "iopub.status.busy": "2023-07-02T17:41:14.091275Z",
     "iopub.status.idle": "2023-07-02T17:41:14.099857Z",
     "shell.execute_reply": "2023-07-02T17:41:14.098988Z"
    },
    "papermill": {
     "duration": 0.023705,
     "end_time": "2023-07-02T17:41:14.102047",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.078342",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 2, \"questionId\": \"2_VariableSwap\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> The most straightforward solution is to use a third variable to temporarily store one of the old values. e.g.:\n",
       "\n",
       "    tmp = a\n",
       "    a = b\n",
       "    b = tmp\n",
       "\n",
       "If you've read lots of Python code, you might have seen the following trick to swap two variables in one line:\n",
       "\n",
       "    a, b = b, a\n",
       "\n",
       "We'll demystify this bit of Python magic later when we talk about *tuples*."
      ],
      "text/plain": [
       "Solution: The most straightforward solution is to use a third variable to temporarily store one of the old values. e.g.:\n",
       "\n",
       "    tmp = a\n",
       "    a = b\n",
       "    b = tmp\n",
       "\n",
       "If you've read lots of Python code, you might have seen the following trick to swap two variables in one line:\n",
       "\n",
       "    a, b = b, a\n",
       "\n",
       "We'll demystify this bit of Python magic later when we talk about *tuples*."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "q2.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "43fea5f5",
   "metadata": {
    "papermill": {
     "duration": 0.011855,
     "end_time": "2023-07-02T17:41:14.126244",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.114389",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<hr/>\n",
    "\n",
    "# 3a.\n",
    "\n",
    "Add parentheses to the following expression so that it evaluates to 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1adaf063",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:14.152286Z",
     "iopub.status.busy": "2023-07-02T17:41:14.151615Z",
     "iopub.status.idle": "2023-07-02T17:41:14.158328Z",
     "shell.execute_reply": "2023-07-02T17:41:14.157284Z"
    },
    "papermill": {
     "duration": 0.022082,
     "end_time": "2023-07-02T17:41:14.160338",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.138256",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(5 - 3) // 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "456a7e7e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:14.186087Z",
     "iopub.status.busy": "2023-07-02T17:41:14.185683Z",
     "iopub.status.idle": "2023-07-02T17:41:14.194184Z",
     "shell.execute_reply": "2023-07-02T17:41:14.193265Z"
    },
    "papermill": {
     "duration": 0.02422,
     "end_time": "2023-07-02T17:41:14.196274",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.172054",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 4, \"questionId\": \"3.1_ArithmeticParensEasy\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint:</span> Following its default \"BEDMAS\"-like rules for order of operations, Python will first divide 3 by 2, then subtract the result from 5. You need to add parentheses to force it to perform the subtraction first."
      ],
      "text/plain": [
       "Hint: Following its default \"BEDMAS\"-like rules for order of operations, Python will first divide 3 by 2, then subtract the result from 5. You need to add parentheses to force it to perform the subtraction first."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "q3.a.hint()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "17f3b452",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:14.222731Z",
     "iopub.status.busy": "2023-07-02T17:41:14.222207Z",
     "iopub.status.idle": "2023-07-02T17:41:14.230247Z",
     "shell.execute_reply": "2023-07-02T17:41:14.229275Z"
    },
    "papermill": {
     "duration": 0.023493,
     "end_time": "2023-07-02T17:41:14.232424",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.208931",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 4, \"questionId\": \"3.1_ArithmeticParensEasy\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> \n",
       "```python\n",
       "(5 - 3) // 2\n",
       "```"
      ],
      "text/plain": [
       "Solution: \n",
       "```python\n",
       "(5 - 3) // 2\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Check your answer (Run this code cell to receive credit!)\n",
    "q3.a.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e59c2b1f",
   "metadata": {
    "papermill": {
     "duration": 0.012448,
     "end_time": "2023-07-02T17:41:14.256776",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.244328",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 3b.  <span title=\"A bit spicy\" style=\"color: darkgreen \">🌶️</span>\n",
    "\n",
    "<small>Questions, like this one, marked a spicy pepper are a bit harder.</small>\n",
    "\n",
    "Add parentheses to the following expression so that it evaluates to 0."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "49685e9e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:14.283528Z",
     "iopub.status.busy": "2023-07-02T17:41:14.283139Z",
     "iopub.status.idle": "2023-07-02T17:41:14.289473Z",
     "shell.execute_reply": "2023-07-02T17:41:14.288418Z"
    },
    "papermill": {
     "duration": 0.022437,
     "end_time": "2023-07-02T17:41:14.291617",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.269180",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "8 - 3 * 2 - (1 + 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e144f357",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:14.319648Z",
     "iopub.status.busy": "2023-07-02T17:41:14.319342Z",
     "iopub.status.idle": "2023-07-02T17:41:14.327475Z",
     "shell.execute_reply": "2023-07-02T17:41:14.326625Z"
    },
    "papermill": {
     "duration": 0.025382,
     "end_time": "2023-07-02T17:41:14.329408",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.304026",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 4, \"questionId\": \"3.2_ArithmeticParensHard\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint:</span> You may need to use several pairs of parentheses."
      ],
      "text/plain": [
       "Hint: You may need to use several pairs of parentheses."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "q3.b.hint()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "de1b2840",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:14.356952Z",
     "iopub.status.busy": "2023-07-02T17:41:14.356598Z",
     "iopub.status.idle": "2023-07-02T17:41:14.364416Z",
     "shell.execute_reply": "2023-07-02T17:41:14.363387Z"
    },
    "papermill": {
     "duration": 0.024431,
     "end_time": "2023-07-02T17:41:14.366556",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.342125",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 4, \"questionId\": \"3.2_ArithmeticParensHard\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> `(8 - 3) * (2 - (1 + 1))` is one solution. There may be others."
      ],
      "text/plain": [
       "Solution: `(8 - 3) * (2 - (1 + 1))` is one solution. There may be others."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Check your answer (Run this code cell to receive credit!)\n",
    "q3.b.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b24a1ba3",
   "metadata": {
    "papermill": {
     "duration": 0.013541,
     "end_time": "2023-07-02T17:41:14.393289",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.379748",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<hr/>\n",
    "\n",
    "# 4. \n",
    "Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves.\n",
    "For the sake of their friendship, any candies left over will be smashed. For example, if they collectively\n",
    "bring home 91 candies, they'll take 30 each and smash 1.\n",
    "\n",
    "Write an arithmetic expression below to calculate how many candies they must smash for a given haul."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c458cb7f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:14.423457Z",
     "iopub.status.busy": "2023-07-02T17:41:14.422418Z",
     "iopub.status.idle": "2023-07-02T17:41:14.433258Z",
     "shell.execute_reply": "2023-07-02T17:41:14.432516Z"
    },
    "papermill": {
     "duration": 0.027906,
     "end_time": "2023-07-02T17:41:14.435369",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.407463",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "307\n",
      "102\n",
      "306\n"
     ]
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.25, \"interactionType\": 1, \"questionType\": 1, \"questionId\": \"4_CandySplitting\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Variables representing the number of candies collected by alice, bob, and carol\n",
    "alice_candies = 121\n",
    "bob_candies = 77\n",
    "carol_candies = 109\n",
    "\n",
    "total_initial = (alice_candies + bob_candies + carol_candies)\n",
    "print(total_initial)\n",
    "\n",
    "# Your code goes here! Replace the right-hand side of this assignment with an expression\n",
    "# involving alice_candies, bob_candies, and carol_candies\n",
    "equal_candies = (alice_candies + bob_candies + carol_candies) // 3\n",
    "print(equal_candies)\n",
    "\n",
    "\n",
    "total_candies = equal_candies * 3\n",
    "print(total_candies)\n",
    "to_smash = total_initial - total_candies\n",
    "\n",
    "# Check your answer\n",
    "q4.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9320a12f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2023-07-02T17:41:14.464046Z",
     "iopub.status.busy": "2023-07-02T17:41:14.463699Z",
     "iopub.status.idle": "2023-07-02T17:41:14.472697Z",
     "shell.execute_reply": "2023-07-02T17:41:14.471919Z"
    },
    "papermill": {
     "duration": 0.025503,
     "end_time": "2023-07-02T17:41:14.474749",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.449246",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 1, \"questionId\": \"4_CandySplitting\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint 1:</span> You'll probably want to use the modulo operator, `%`.\n",
       "(For another hint, call `.hint(2)`)"
      ],
      "text/plain": [
       "Hint 1: You'll probably want to use the modulo operator, `%`.\n",
       "(For another hint, call `.hint(2)`)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 1, \"questionId\": \"4_CandySplitting\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> \n",
       "```python\n",
       "(alice_candies + bob_candies + carol_candies) % 3\n",
       "```"
      ],
      "text/plain": [
       "Solution: \n",
       "```python\n",
       "(alice_candies + bob_candies + carol_candies) % 3\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "q4.hint()\n",
    "q4.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d23eed27",
   "metadata": {
    "papermill": {
     "duration": 0.013956,
     "end_time": "2023-07-02T17:41:14.502893",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.488937",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Keep Going\n",
    "\n",
    "Next up, you'll **[learn to write new functions and understand functions others write](https://www.kaggle.com/colinmorris/functions-and-getting-help)**. This will make you at least 10 times more productive as a Python programmer. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6bf1a901",
   "metadata": {
    "papermill": {
     "duration": 0.013715,
     "end_time": "2023-07-02T17:41:14.530533",
     "exception": false,
     "start_time": "2023-07-02T17:41:14.516818",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "---\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "*Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/python/discussion) to chat with other learners.*"
   ]
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
   "version": "3.10.10"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 12.871545,
   "end_time": "2023-07-02T17:41:15.264481",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2023-07-02T17:41:02.392936",
   "version": "2.4.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
