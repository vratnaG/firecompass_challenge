import React, { useState, useEffect } from 'react'
import { baseurl } from "../configure.js"
import axios from "axios"
import "../style/home.css"
import AddPerson from './AddPerson.js'

function Home() {

    const [lobbys, setLobbys] = useState(null)
    const [add, setAdd] = useState(false)
    const [winner, setWinner] = useState(null)
    const [currlobby, setCurrLobby] = useState({})
    useEffect(() => {
        axios.get(baseurl + 'lotery/lobby/')
            .then((res) => {
                setLobbys(res.data)
                console.log(lobbys)
            })
            .catch((err) => {
                alert(err.messages)
            })
        axios.get(baseurl + 'lotery/winners/')
            .then((res) => {
                setWinner(res.data)
                console.log(winner)
            })
            .catch((err) => {
                alert(err.messages)
            })
    }, [])

    function total_housing() {
        let total = 0
        winner.data.map((data) => { total = total + data.House })
        return total
    }
    return (
        <div>
            {!add && <div><div className="title">Loby List</div>
                {winner && <div>House Collection:{total_housing()}</div>}
                <div className="lobby-header">
                    <div>Name</div>
                    <div>Entry_Fee</div>
                    <div>Capcity</div>
                </div>
                {lobbys && lobbys.data.map((data) => <div id={data.id} className="lobby-list" onClick={() => { setAdd(true); setCurrLobby(data) }}>
                    <div>{data.Name}</div>
                    <div>{data.Entry_Fee}</div>
                    <div>{data.Capcity}</div>
                </div>)}</div>}
            {add && <AddPerson setAdd={setAdd} lobby={currlobby} />
            }

        </div>
    )
}

export default Home
