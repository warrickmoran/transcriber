import pytest

from audio.transcribe_audio import (
    transcribe_audio,
    meeting_minutes,
    abstract_summary_extraction,
    key_points_extraction,
    action_item_extraction,
    sentiment_analysis,
)

@pytest.fixture
def sample_transcription():
    # Provide a sample transcription for testing
    return "Your sample transcription goes here."

def test_transcribe_audio(sample_transcription):
    # Test transcribe_audio function
    result = transcribe_audio("path/to/your/audio/file.wav")
    assert isinstance(result, str)

def test_abstract_summary_extraction(sample_transcription):
    # Test abstract_summary_extraction function
    result = abstract_summary_extraction(sample_transcription)
    assert isinstance(result, str)

# Similar tests for key_points_extraction, action_item_extraction, sentiment_analysis

def test_meeting_minutes(sample_transcription):
    # Test meeting_minutes function
    result = meeting_minutes(sample_transcription)
    assert isinstance(result, dict)

def test_save_as_docx(sample_transcription, tmp_path):
    # Test save_as_docx function
    minutes = meeting_minutes(sample_transcription)
    filename = tmp_path / "test_meeting_minutes.docx"
    save_as_docx(minutes, filename)
    assert filename.exists()
