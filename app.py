import gradio as gr
import joblib
import warnings
import numpy as np

warnings.filterwarnings('ignore')

# Load the trained model
model = joblib.load('C:\\Users\\USER\\Documents\\Received\\PYTHON\\Xin_Yin\\WriteUp-Result_3-Research\\model.joblib')

# Define the prediction function
def UniaxialCompressiveStrength(SRn, Vp, Is):
    X = np.array([SRn, Vp, Is])
    prediction = model.predict(X.reshape(1, -1))
    return prediction

outputs = gr.outputs.Textbox()
iface = gr.Interface(fn=UniaxialCompressiveStrength, inputs=['number', 'number', 'number'], outputs=outputs, description="This is a Uniaxial Compressive Strength Prediction Model")
iface.launch(share=True)

# Start the Gradio interface
iface.launch()





import gradio as gr
import joblib
import warnings
warnings.filterwarnings('ignore')

# Load the trained model
model = joblib.load('C:\\Users\\USER\\Documents\\Received\\PYTHON\\Xin_Yin\\WriteUp-Result_3-Research\\model.joblib')

# Define the prediction function

def UniaxialCompressiveStrength(SRn, Vp, Is):
    X = np.array([SRn, Vp, Is])
    prediction = RF.predict(X.reshape(1, -1))
    return prediction

outputs = gr.outputs.Textbox()
iface = gr.Interface(fn=UniaxialCompressiveStrength, inputs=['number','number','number'], outputs=outputs,description="This is a Uniaxial Compressive Strength Prediction Model")
iface.launch(share=True)

# Start the Gradio interface
iface.launch()
