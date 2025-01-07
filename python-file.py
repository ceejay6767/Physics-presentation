import matplotlib.pyplot as plt
import numpy as np

class SoundWaveApp:
    def __init__(self):
        print("Physics Project: Enhancing Classroom Acoustics")
        self.run_app()

    def run_app(self):
        print("\nProblem:")
        print("Students sitting far in a classroom can't properly hear the teacher during lessons.")
        print("This is due to sound waves dissipating before reaching them.")

        print("\nSolution:")
        print("Installing sonorous plates to bounce sound waves effectively, ensuring that sound reaches all students in the classroom.")

        # Display both visualizations
        self.visualize_both()

    def visualize_both(self):
        # Generate sound wave visualization without plates
        fig1, ax1 = plt.subplots(figsize=(5, 4))
        x = np.linspace(0, 10, 400)
        y = np.sin(2 * np.pi * 0.5 * x) * np.exp(-0.1 * x)
        ax1.plot(x, y, label="Dissipating Sound Waves")
        ax1.set_title("Sound Waves Without Sonorous Plates")
        ax1.set_xlabel("Distance (m)")
        ax1.set_ylabel("Amplitude")
        ax1.legend()

        # Generate sound wave visualization with plates
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        y_reflected = np.sin(2 * np.pi * 0.5 * (10 - x)) * np.exp(-0.1 * (10 - x))
        ax2.plot(x, y, label="Original Sound Waves")
        ax2.plot(x, y + y_reflected, label="Amplified Sound Waves with Reflection")
        ax2.set_title("Sound Waves with Sonorous Plates")
        ax2.set_xlabel("Distance (m)")
        ax2.set_ylabel("Amplitude")
        ax2.legend()

        # Show both figures simultaneously
        plt.show(block=False)

        # Keep the plots open for a specified time (e.g., 5 seconds) or until manually closed
        plt.pause(120)
        plt.close(fig1)
        plt.close(fig2)

if __name__ == "__main__":
    SoundWaveApp()
