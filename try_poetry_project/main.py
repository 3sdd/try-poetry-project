import pendulum


if __name__=="__main__":
    now=pendulum.now()

    print(now.to_iso8601_string())
