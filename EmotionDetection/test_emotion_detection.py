import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I am so happy and joyful")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_anger(self):
        result = emotion_detector("I am furious and angry")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_disgust(self):
        result = emotion_detector("This is disgusting")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_sadness(self):
        result = emotion_detector("I feel very sad")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_fear(self):
        result = emotion_detector("I am terrified")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()