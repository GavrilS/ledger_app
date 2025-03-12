import ledger_app

def main():
    app = ledger_app.create_app()

    app.run(debug=True)


if __name__=='__main__':
    main()