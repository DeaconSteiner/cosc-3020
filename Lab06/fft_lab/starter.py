"""
FFT Lab Starter (COSC 3020) — Python

You may use numpy for reading files and plotting if you want,
but you must implement fft_recursive() and ifft_recursive()
(without calling np.fft.fft/ifft inside those functions).

Run:
    python starter.py

Deliverables:
    - Fill in TODOs below.
    - Produce outputs described in README.pdf.
"""

from __future__ import annotations

import cmath
from typing import Dict, List, Tuple

import numpy as np

FS = 4096  # sampling rate (Hz)

NOTE_TABLE: Dict[str, float] = {
    "B3": 246.94,
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "C5": 523.25,
}


def _is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1) == 0)


def fft_recursive(x: np.ndarray) -> np.ndarray:
    """
    Cooley–Tukey radix-2 FFT (recursive).
    Input: 1D complex or real array length N (power of two)
    Output: 1D complex array length N (DFT of x)

    TODO: implement without using np.fft.fft
    """
    N = x.shape[0]
    if not _is_power_of_two(N):
        raise ValueError("N must be a power of two")

    w = cmath.exp(-1j * 2 * cmath.pi / N)

    # Base case
    if N == 1:
        return x.astype(complex)

    # TODO: split even/odd, recursively FFT, combine with twiddle factors
    # Split
    xe = x[::2]
    xo = x[1::2]

    ## Recurse
    xef = fft_recursive(xe)
    xof = fft_recursive(xo)

    # Combine
    xf = np.zeros(N, dtype=complex)
    wi = 1
    for i in range(len(xe)):
        xf[i] = xef[i] + wi * xof[i]
        xf[i + N // 2] = xef[i] - wi * xof[i]
        wi = wi * w
    return xf


def ifft_recursive(X: np.ndarray) -> np.ndarray:
    """
    Inverse FFT using your fft_recursive.
    Convention: ifft(fft(x)) == x (within floating-point error)

    Hint: One easy way:
        ifft(X) = conj( fft(conj(X)) ) / N

    TODO: implement without using np.fft.ifft
    """
    N = X.shape[0]
    if not _is_power_of_two(N):
        raise ValueError("N must be a power of two")

    # TODO
    return np.conjugate(fft_recursive(np.conjugate(X))) / N


def dominant_frequencies(x: np.ndarray, k: int = 3) -> List[Tuple[float, float]]:
    """
    Return top-k (frequency_hz, magnitude) peaks for a real-valued signal segment x.
    Uses your FFT implementation.

    Notes:
      - Only return frequencies in [0, FS/2] (positive frequencies)
      - Ignore the DC component at 0 Hz
    """
    N = len(x)
    X = fft_recursive(x.astype(complex))
    mags = np.abs(X)[: N // 2 + 1]  # keep non-negative freqs
    freqs = np.arange(0, N // 2 + 1) * (FS / N)

    mags[0] = 0.0  # ignore DC

    # TODO: pick top-k peaks by magnitude
    # Return list sorted by magnitude descending
    peaks = np.argsort(mags)[-k:][::-1]

    top_freqs = freqs[peaks]
    top_mags = mags[peaks]

    return list(zip(top_freqs, top_mags))


def closest_notes(freqs: List[Tuple[float, float]], tol_hz: float = 8.0) -> List[str]:
    """
    Map detected peak frequencies to nearest named notes in NOTE_TABLE.
    Only include matches within tol_hz.
    """
    out: List[str] = []
    for f, _mag in freqs:
        best_note = None
        best_err = float("inf")
        for name, nf in NOTE_TABLE.items():
            err = abs(f - nf)
            if err < best_err:
                best_err = err
                best_note = name
        if best_note is not None and best_err <= tol_hz and best_note not in out:
            out.append(best_note)
    return out


def denoise_by_threshold(x: np.ndarray, keep_ratio: float = 0.15) -> np.ndarray:
    """
    Simple frequency-domain denoising:
      - FFT
      - keep coefficients whose magnitude >= keep_ratio * max_magnitude
      - zero out the rest
      - inverse FFT

    Uses your FFT and IFFT.

    Returns real-valued denoised signal.
    """
    N = len(x)
    X = fft_recursive(x.astype(complex))
    mags = np.abs(X)
    thresh = keep_ratio * np.max(mags)

    # TODO: zero out small coefficients, keep big ones
    # Then inverse transform, return np.real(...)
    transform = np.where(mags >= thresh, X, 0)
    inverse = ifft_recursive(transform)
    return np.real(inverse)


def main():
    data = np.load("data/sample_waveform.npy")
    seg_len = 2048  # 0.5s per segment at FS=4096
    assert len(data) % seg_len == 0
    num_segs = len(data) // seg_len

    print(f"Loaded waveform: {len(data)} samples, {num_segs} segments of {seg_len}.")

    all_notes = []
    denoised = np.zeros_like(data, dtype=float)

    for i in range(num_segs):
        seg = data[i * seg_len : (i + 1) * seg_len].astype(float)

        peaks = dominant_frequencies(seg, k=3)
        notes = closest_notes(peaks)
        all_notes.append(notes)

        denoised_seg = denoise_by_threshold(seg, keep_ratio=0.15)
        denoised[i * seg_len : (i + 1) * seg_len] = denoised_seg

        print(
            f"Segment {i + 1}: peaks={[(round(f, 1), round(m, 2)) for f, m in peaks]} -> notes={notes}"
        )

    np.savetxt("denoised_waveform.csv", denoised, delimiter=",")
    print("\nWrote denoised_waveform.csv")

    # Expected rough notes (order within each segment may vary):
    # 1: ['A4']
    # 2: ['C4','E4','G4']
    # 3: ['D4']
    # 4: ['A4']
    # 5: ['C5','A4']
    print("\nYour detected notes per segment:")
    for i, notes in enumerate(all_notes, 1):
        print(f"  {i}: {notes}")


if __name__ == "__main__":
    main()
