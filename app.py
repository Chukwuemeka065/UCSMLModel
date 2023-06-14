{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "417c059e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running on local URL:  http://127.0.0.1:7860\n",
      "Running on public URL: https://7006cf86b3a43286be.gradio.live\n",
      "\n",
      "This share link expires in 72 hours. For free permanent hosting and GPU upgrades (NEW!), check out Spaces: https://huggingface.co/spaces\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"https://7006cf86b3a43286be.gradio.live\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rerunning server... use `close()` to stop if you need to change `launch()` parameters.\n",
      "----\n",
      "Running on local URL:  http://127.0.0.1:7860\n",
      "\n",
      "To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7860/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import gradio as gr\n",
    "import joblib\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "\n",
    "# Load the trained model\n",
    "model = joblib.load('C:\\\\Users\\\\USER\\\\Documents\\\\Received\\\\PYTHON\\\\Xin_Yin\\\\WriteUp-Result_3-Research\\\\model.joblib')\n",
    "\n",
    "# Define the prediction function\n",
    "\n",
    "def UniaxialCompressiveStrength(SRn, Vp, Is):\n",
    "    X = np.array([SRn, Vp, Is])\n",
    "    prediction = RF.predict(X.reshape(1, -1))\n",
    "    return prediction\n",
    "\n",
    "outputs = gr.outputs.Textbox()\n",
    "iface = gr.Interface(fn=UniaxialCompressiveStrength, inputs=['number','number','number'], outputs=outputs,description=\"This is a Uniaxial Compressive Strength Prediction Model\")\n",
    "iface.launch(share=True)\n",
    "\n",
    "# Start the Gradio interface\n",
    "iface.launch()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
