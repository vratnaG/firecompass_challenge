import React from 'react'
import "../style/personlist.css"
import axios from "axios"
import { baseurl } from "../configure"

function PersonList(props) {
    function filter_person(id) {
        return props.persons.data.filter(data => data.id !== id);
    }

    function select_person(id) {
        axios.put(baseurl + 'lotery/entry_deduction/' + id, { "Lobby_id": props.lobby.id })
            .then((res) => {
                if (res.data.code === 200) {
                    let selectedNew = [res.data.data]
                    let selected = [...props.selected, ...selectedNew]
                    props.setSelected(selected)

                    let persons = props.persons
                    persons.data = filter_person(id)
                    props.setPersons({ ...props.persons, persons })
                    props.setList(false)
                }
                else {
                    alert(res.data.message)
                }
            })
            .catch((err) => {
                alert(err.messages)
            })
    }

    function manage_all(id) {

        if (props.selected.length < props.lobby.Capcity) {
            select_person(id)
        }
        else {
            alert('lobby full')
            props.setList(false)
        }
    }

    return (
        <div>
            {!props.persons.data.length && <div className="close" onClick={() => props.setList(false)}>close</div>}
            <div className="title-ls">Person list</div>
            <div className="person-header">
                <div>Name</div>
                <div>Amount</div>
            </div>
            {
                props.persons.data && props.persons.data.map((data) => <div id={data.id} className="person-list" onClick={() => manage_all(data.id)}>
                    <div>{data.Name}</div>
                    <div>{data.Amount}</div>
                </div>)
            }

        </div>
    )
}

export default PersonList
