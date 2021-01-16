import React, { useState, useEffect } from 'react'
import axios from "axios"
import { baseurl } from "../configure"
import "../style/winner.css"
function Winner(props) {
    const [state, setstate] = useState(false)
    console.log(props.winner)
    useEffect(() => {
        axios.post(baseurl + 'lotery/winners/', {
            "Lobby_id": props.lobby.id,
            "Winner_id": props.winner.id
        })
            .then((res) => {
                if (res.data.code === 200) {
                    setstate(true)
                }
                else {
                    setstate(false)
                }

            })
            .catch((err) => {
                alert(err.messages)
            })
    }, [])

    return (
        <div className="winner">
            {state && <div>Winner:{props.winner.Name}</div>}
        </div>
    )
}

export default Winner
