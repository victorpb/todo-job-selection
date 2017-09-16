    Vue.component('todo-item')

    var app = new Vue({
        delimiters: ['[[', ']]'],
        el: '#todolist',
        data: {
            tasks: [],
            description: '',
            edit: false,
            active: true
        },
        mounted() {
            axios.get('api/v1/tasks/').then(response => { this.tasks = response.data })
        },
        methods: {

            doneTask: function(index, id, description) {
                this.tasks[index].done = true
                
                axios.put('api/v1/tasks/' + id + '/', { description: description, done: true })
            },
            undoneTask: function(index, id, description) {
                this.tasks[index].done = false
                axios.put('api/v1/tasks/' + id + '/', { description: description, done: false })
            },
            deleteTask: function(index, id) {
                console.log('oi')
                this.tasks.splice(index, 1)
                axios.delete('api/v1/tasks/' + id + '/')
            },
            addTask: function(description) {
                this.tasks.push({ description: description })
                axios.post('api/v1/tasks/', { description: description })
                this.description = ''
            },
            editTask: function(id, description) {
                axios.put('api/v1/tasks/' + id + '/', { description: description, done: false })
            }
        }
    })
