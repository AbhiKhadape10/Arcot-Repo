from ml_service import predict

def test_predict():
    result = predict("test_data")
    assert result == "Prediction result"
