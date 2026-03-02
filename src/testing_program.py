from chaos_game import ChaosGame

shape = ChaosGame(5, 0.618)
print("Pentagon corners:")
for i, corner in enumerate(shape.corners):
    print(f"  Corner {i}: {corner}")