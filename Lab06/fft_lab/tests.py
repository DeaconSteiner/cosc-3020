"""
Basic autograder-style checks for FFT Lab.

Run:
    python tests.py

These tests are intentionally lightweight and focus on correctness.
"""
import numpy as np
import starter

def test_fft_matches_numpy():
    rng = np.random.default_rng(0)
    for N in [2,4,8,16,64,256]:
        x = rng.normal(size=N) + 1j*rng.normal(size=N)
        X1 = starter.fft_recursive(x.copy())
        X2 = np.fft.fft(x)
        assert np.allclose(X1, X2, atol=1e-6), f"FFT mismatch for N={N}"

def test_ifft_roundtrip():
    rng = np.random.default_rng(1)
    for N in [2,8,32,128]:
        x = rng.normal(size=N)
        X = starter.fft_recursive(x.astype(complex))
        xr = starter.ifft_recursive(X)
        assert np.allclose(xr, x, atol=1e-6), f"IFFT roundtrip mismatch for N={N}"

def test_note_detection_on_first_segment():
    data = np.load("data/sample_waveform.npy")
    seg = data[:2048].astype(float)
    peaks = starter.dominant_frequencies(seg, k=3)
    notes = starter.closest_notes(peaks, tol_hz=10.0)
    assert "A4" in notes, f"Expected A4 in detected notes, got {notes}"

def main():
    test_fft_matches_numpy()
    test_ifft_roundtrip()
    test_note_detection_on_first_segment()
    print("All tests passed ✅")

if __name__ == "__main__":
    main()
