from flask import Flask, render_template, request

app = Flask(__name__)

RATE_PER_HOUR = 150000  # Rp per hour, per group
TOURS = ["Braga Heritage Walk", "Asia-Afrika Story Walk", "Sunda Food & Culture Walk"]
VALID_HOURS = (2, 3, 4)
VALID_GUESTS = (1, 2, 3, 4)


def rupiah(amount):
    return "Rp" + f"{amount:,}".replace(",", ".")


@app.route("/", methods=["GET", "POST"])
def index():
    form = {"tour": TOURS[0], "hours": "3", "guests": "2", "date": ""}
    result = None
    error = None

    if request.method == "POST":
        form["tour"] = request.form.get("tour", "").strip()
        form["hours"] = request.form.get("hours", "").strip()
        form["guests"] = request.form.get("guests", "").strip()
        form["date"] = request.form.get("date", "").strip()

        try:
            hours = int(form["hours"])
            guests = int(form["guests"])
        except ValueError:
            hours = guests = None

        if form["tour"] not in TOURS:
            error = "Please choose one of the three tours."
        elif hours not in VALID_HOURS:
            error = "Please choose a duration of 2, 3, or 4 hours."
        elif guests not in VALID_GUESTS:
            error = "We welcome private groups of 1 to 4 guests. Please enter a number from 1 to 4."
        else:
            result = {
                "amount": rupiah(hours * RATE_PER_HOUR),
                "summary": f"{form['tour']}, {hours} hours, {guests} guest(s)",
                "date": form["date"],
            }

    return render_template("index.html", form=form, tours=TOURS, result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
