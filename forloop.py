# Theater has 5 rows and 6 seats per row
rows = 5
seats_per_row = 6

# Create a 2D list (matrix) with all seats available (marked as 'O')
seating = [['O' for _ in range(seats_per_row)] for _ in range(rows)]

def display_seats():
    print("\n🎟️ Theater Seating Arrangement:")
    print("   " + " ".join([f"S{i+1}" for i in range(seats_per_row)]))  # Seat headers
    for i in range(rows):
        print(f"R{i+1} " + " ".join(seating[i]))

def book_seat(row, seat):
    if seating[row-1][seat-1] == 'X':
        print("⛔ Seat already booked.")
    else:
        seating[row-1][seat-1] = 'X'
        print("✅ Seat booked successfully!")

# --- Simulation ---
display_seats()

# Booking some seats
book_seat(2, 3)
book_seat(4, 1)
book_seat(2, 3)  # Trying to book again

# Show updated seating
display_seats()
