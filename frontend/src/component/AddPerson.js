import React, { useState, useEffect } from 'react'
import "../style/addperson.css"
import axios from "axios"
import { baseurl } from "../configure"
import PersonList from './PersonList'
import Winner from './Winner'
function AddPerson(props) {
    const [persons, setPersons] = useState(null)
    const [list, setList] = useState(false)
    const [selected, setSelected] = useState([])
    const [showwinner, setShowWinner] = useState(false)
    useEffect(() => {
        axios.get(baseurl + 'lotery/person/')
            .then((res) => {
                setPersons(res.data)
                console.log(persons)
            })
            .catch((err) => {
                alert(err.messages)
            })
    }, [])


    function winner_decide() {
        if (selected.length < props.lobby.Capcity) {
            alert('room not full')
        }
        else {
            setShowWinner(true)
        }
    }

    function getRandomInt(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    console.log('selectet', selected)
    return (
        <div>
            {!showwinner && !list && <div>
                <div className="close" onClick={() => props.setAdd(false)}>close</div>
                <div className="add-button"><button onClick={() => setList(true)}>Add</button></div>
                <div> selected</div>
                <div className="person-header">
                    <div>Name</div>
                    <div>Amount</div>
                </div>
                {
                    selected && selected.map((data) => <div id={data.id} className="person-list" >
                        <div>{data.Name}</div>
                        <div>{data.Amount}</div>
                    </div>)
                }
                <div className="add-button"><button onClick={() => winner_decide()}>Start</button></div>
            </div>
            }
            {
                !showwinner && list && <PersonList persons={persons} selected={selected} lobby={props.lobby} setSelected={setSelected} setPersons={setPersons} setList={setList} />
            }
            {
                showwinner && <Winner lobby={props.lobby} winner={selected[getRandomInt(0, selected.length)]} />
            }
        </div>
    )
}

export default AddPerson
